driver = set_webdriver(web_visual=True)
get_images(driver, ['고양이', '고양이 얼굴', '고양이 꼬리', '강아지'], ['naver', 'google'], 1001)  # naver maximum items 1000
driver.close()

import os                       # 파일경로에 사용
import time                     # 딜레이를 줄 필요가 있을 때 sleep 함수
import datetime                 # 파일경로
import ssl                      # 주소가 https 인 경우, urlretrieve로 이미지 다운받을 때 에러 처리

from selenium import webdriver      # browser와 연동하는데 씀
from urllib.parse import quote_plus # 한국어 검색 처리
import urllib.request               # urlretrieve 함수 사용(이미지 다운로드)
from selenium.webdriver.common.keys import Keys # PAGE_DOWN키를 전송할때 사용
# exceptions 예외 처리모듈
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException,  ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from urllib.error import URLError, HTTPError

class TrialError(Exception):
    def __init__(self):
         super().__init__('TRIAL EXCESS')

def _no_more_img_click(drv):
    try:

        drv.find_element_by_css_selector('#_sau_imageTab > div.photowall._photoGridWrapper > div.more_img > a').click()
    except ElementNotInteractableException:
        if drv.find_element_by_css_selector('#_sau_imageTab > div.message_bottom._noMore'):
            print('ElementNotInteractableException - No More Image')
        else:
            print('ElementNotInteractableException')
        return False

    print('CLICK SUCCESS')
    return True

def _iidx_grid_box(drv, iidx):
    try:
        item = drv.find_element_by_css_selector('div.photowall._photoGridWrapper > div.photo_grid._box[data-box-idx="' + str(iidx) + '"]')

    except NoSuchElementException:
        print('No Grid Box(' + str(iidx) + ') created.')
        # drv.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        if _no_more_img_click(drv):
            return _iidx_grid_box(drv, iidx)
        else:
            return False
    except TrialError:
        print('TrialError')
        return False
    print('IIDX GRID BOX OPENED')
    return item

def _retrieve2(drv, keyword, path, gbox, idx, acc, trial=0, max_trial=20):
    try:
        # 무한루프 방지
        if trial > max_trial:
             raise TrialError(trial)
        # 저장경로 
        if not (os.path.isdir(path)):
            os.makedirs(os.path.join(path))
        # 이미지 링크주소를 받아온다.
        img = gbox.find_element_by_css_selector('div > div:nth-child(' + str(idx) + ') > a > img._img').get_attribute('src')
        # 저장경로에 이미지 저장
        urllib.request.urlretrieve(img, path + '/' + keyword + str(acc) + '.jpg')

    except URLError:
        # URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
        print('ERROR URLError in _retrieve', trial)
        ssl._create_default_https_context = ssl._create_unverified_context
        trial += 1
        _retrieve2(img, keyword, path, gbox, idx, acc, trial)
    except HTTPError:
        # TODO 나중에 찾아보자
         print('ERROR HTTPError in _retrieve', img, trial)
         trial += 1
         time.sleep(1)
         _retrieve2(img, keyword, path, gbox, idx, acc, trial)
    except TrialError:
         driver.close()

def _inner_loop_naver_driver(drv, keyword, path, wanted, gbox, inner_idx=0, idx=1, acc=0):
    # 원하는 갯수만큼 받았으면 종료
    if acc == wanted:
        return True, acc

    # 그리드 안되고, 원하는 갯수만큼보다 적게 다운받은 경우 False
    if not gbox:
        return False, acc
    try:
        _retrieve2(drv, keyword, path, gbox, idx, acc)
    except NoSuchElementException: # 그리드박스내 이미지 idx 가 over
        idx = 1
        inner_idx += 1
        gbox = _iidx_grid_box(drv, inner_idx)
    else:                       # 순차적으로 다운받음
        acc += 1
        idx += 1
    return _inner_loop_naver_driver(drv, keyword, path, wanted, gbox, inner_idx, idx, acc)

def _loop_naver_driver(drv, keyword, path, wanted):
    time.sleep(2)               # 초기로딩 지연이 종종 있어서 2초가 sleep후 진행
    return _inner_loop_naver_driver(drv, keyword, path, wanted, _iidx_grid_box(drv, 0))

def _get_naver_items(drv, url, keyword, host, wanted):
    drv.get(url + quote_plus(keyword))
    path = host + '_images/' + str(datetime.date.today()) + '/' + keyword
    p, new_items = _loop_naver_driver(drv, keyword, path, wanted)
    print(p)

    return new_items

def set_webdriver(web_driver=None, web_visual=None):
    if web_driver is None:
        chrome_options = webdriver.ChromeOptions()
        if web_visual is None:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome('/Users/sroh/Downloads/chromedriver', options=chrome_options)
    else:
        driver = web_driver

    return driver

def inner_loop_google_driver(drv, keyword, path, wanted, idx=1, trial=0, max_trial=50):
    try:
        if trial > max_trial:
            raise TrialError(trial)
        # print(drv.find_element_by_css_selector('div.islrc > div:nth-child(' + str(idx) + ') > a.wXeWr.islib.nfEiy.mM5pbd > div > img').is_displayed())
        drv.find_element_by_css_selector('div.islrc > div:nth-child(' + str(idx) + ') > a.wXeWr.islib.nfEiy.mM5pbd > div').click()
    except ElementNotInteractableException: # loaded image not yet
        drv.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        drv.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        drv.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        print(trial, 'ELEMENTNOTINTERACTABLEEXCEPTION AT:', idx)
        trial += 1
        return inner_loop_google_driver(drv, keyword, path, wanted, idx, trial)
    except NoSuchElementException:
        print(trial, 'NOSUCHE: ', idx)
        return False
    except TrialError:
        drv.close()
        return False

    else:
        if idx > wanted:
            return 'OK'
        _retrieve(drv.find_element_by_css_selector('#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div.OUZ5W > div.zjoqD > div > div.v4dQwb > a > img.n3VNCb').get_attribute('src'), keyword, path, idx)
        idx += 1
    return inner_loop_google_driver(drv, keyword, path, wanted, idx)

def loop_google_driver(drv, keyword, path, wanted):
     return inner_loop_google_driver(drv, keyword, path, wanted)

def _get_google_items(drv, url, keyword, host, wanted):
    drv.get(url)
    drv.find_element_by_css_selector('div.a4bIc > input').send_keys(keyword + '\n')

    path = host + '_images/' + str(datetime.date.today()) + '/' + keyword
    new_items = loop_google_driver(drv, keyword, path, wanted)
    return new_items

def _get_images(drv, keyword, host, n_items, 
                d_servs={'naver' : ['https://search.naver.com/search.naver?where=image&sm=tab_jum&query=', _get_naver_items],
                         'google' : ['https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl', _get_google_items]}):
    url = d_servs[host][0]
    fn = d_servs[host][1]
    print(fn(drv, url, keyword, host, n_items))

def _get_images_by_hosts(drv, keyword, hosts, n_items):
     if hosts == []:
         print('HOSTS OK')
     else:
         _get_images(drv, keyword, hosts[0], n_items)
         _get_images_by_hosts(drv, keyword, hosts[1:], n_items)

def get_images(drv, keywords, hosts, n_items):
    if keywords == []:
        print ('KEYWORDS OK')
    else:
        _get_images_by_hosts(drv, keywords[0], hosts, n_items)
        get_images(drv, keywords[1:], hosts, n_items)


def _retrieve(img, keyword, path, idx, trial=0, max_trial=50):
    if not (os.path.isdir(path)):
        os.makedirs(os.path.join(path))
    try:
        if trial > max_trial:
             raise TrialError(trial)
        urllib.request.urlretrieve(img, path + '/' + keyword + str(idx) + '.jpg')
    except URLError:
        # URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local
        print('ERROR URLError in _retrieve', trial)
        ssl._create_default_https_context = ssl._create_unverified_context
        trial += 1
        _retrieve(img, keyword, path, idx, trial)
    except HTTPError:
         print('ERROR HTTPError in _retrieve', img, trial)
         trial += 1
         time.sleep(1)
         _retrieve(img, keyword, path, idx, trial)
    except TrialError:
         driver.close()

def retrieve(imgs, keyword, host):
    path = host + '_images/' + str(datetime.date.today()) + '/' + keyword

    for idx, i in enumerate(imgs):
        _retrieve(i, keyword, path, idx)

driver = set_webdriver(web_visual=True)

get_images(driver, ['고양이'], ['naver'], 10)  # naver maximum items 1000

driver.close()

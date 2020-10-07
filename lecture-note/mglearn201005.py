import urllib.request
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

keyword = quote_plus('고양이')
print(keyword)

import urllib.request
from bs4 import BeautifulSoup

def get_url_from_search_word(sw, q='https://search.naver.com/search.naver?where=image&sm=tab_jum&query='):
    return q + urllib.request.pathname2url(sw)
url = get_url_from_search_word('고양이')
res = urllib.request.urlopen(url).read()
soup = BeautifulSoup(res, 'html.parser')
# print(soup.find('div', {'class' : 'photowall _photoGridWrapper'}))

from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
from selenium.webdriver.common.keys import Keys
import time



# base_url = get_url_from_search_word('고양이')
url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
keyword = '고양이'
base_url = url + quote_plus(keyword)

chrome_options = webdriver.ChromeOptions()
# colab에서는 보이지 않는 상태에서 쓸거기때문에 필요한 옵션임.
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/Users/sroh/Downloads/chromedriver', options=chrome_options)
# driver = webdriver.Chrome('/Users/sroh/Downloads/chromedriver')
driver.get(base_url)

body = driver.find_element_by_css_selector('body')
# def set_web_pages_with_num_images (n_images):
#     n = int(n_images / 50)
#     return
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

imgs = driver.find_elements_by_css_selector('img._img')
# for idx, img in enumerate(imgs):
#     print(idx, img.get_attribute('src')[:3])

count = 0
idx = 0
idx_max = len(imgs)
acc = []
while count < 300:
  if imgs[idx].get_attribute('src')[:4] == 'http':
      # print(idx, count, imgs[idx].get_attribute('src')[:4])
      acc.append(imgs[idx].get_attribute('src'))
      count += 1
  idx += 1
  if idx == idx_max:
      # print("spawn")
      for i in range(10):
          body.send_keys(Keys.PAGE_DOWN)
          time.sleep(1)
      imgs = driver.find_elements_by_css_selector('img._img')
      idx_max = len(imgs)

print(acc[:10])

from selenium import webdriver
  from urllib.request import urlopen
  import urllib.request
  from bs4 import BeautifulSoup as bs
  from urllib.parse import quote_plus
  from selenium.webdriver.common.keys import Keys
  import time
  import os


  # base_url = get_url_from_search_word('고양이')
  url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='

  keyword = '수컷고양이'
  base_url = url + quote_plus(keyword)

  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome('/Users/sroh/Downloads/chromedriver', options=chrome_options)

  driver.get(base_url)
  body = driver.find_element_by_css_selector('body')

  # for i in range(10):
  #     body.send_keys(Keys.PAGE_DOWN)
  #     time.sleep(1)

  # imgs = driver.find_elements_by_css_selector('img._img')
  # count = 0
  # idx = 0
  # idx_max = len(imgs)
  # acc = []
  # while count < 20:
  #   if imgs[idx].get_attribute('src')[:4] == 'http':
  #       # print(idx, count, imgs[idx].get_attribute('src')[:4])
  #       acc.append(imgs[idx].get_attribute('src'))
  #       count += 1
  #       idx += 1
  #       if idx == idx_max:
  #            # print("spawn")
  #            for i in range(10):
  #                body.send_keys(Keys.PAGE_DOWN)
  #                time.sleep(1)
  #            imgs = driver.find_elements_by_css_selector('img._img')
  #            idx_max = len(imgs)


# get_images('고양이')

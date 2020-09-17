#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from selenium import webdriver


# In[22]:


driver = webdriver.Chrome('../driver/chromedriver')
driver.get("http://www.opinet.co.kr/searRgSelect.do")


# //*[@id="quick_ul"]/li[2]/a/span

# In[23]:


xpath ="""//*[@id="quick_ul"]/li[2]/a/span"""
driver.find_element_by_xpath(xpath).click()


# //*[@id="SIGUNGU_NM0"]

# In[24]:


gu_list_raw = driver.find_element_by_xpath("""//*[@id="SIGUNGU_NM0"]""")
gu_list = gu_list_raw.find_elements_by_tag_name("option")


# In[25]:


gu_names = [option.get_attribute("value") for option in gu_list]
gu_names.remove('')
gu_names


# In[19]:


element = driver.find_element_by_id("SIGUNGU_NM0")
element.send_keys(gu_names[1])


# In[27]:


xpath = """//*[@id="searRgSelect"]/span"""#//*[@id="searRgSelect"]/span
element_sel_gu = driver.find_element_by_xpath(xpath).click()


# In[21]:


xpath = """//*[@id="glopopd_excel"]"""#//*[@id="glopopd_excel"]/span
element_get_excel = driver.find_element_by_xpath(xpath).click()


# In[28]:


import time
from tqdm import tqdm_notebook

for gu in tqdm_notebook(gu_names):
    element = driver.find_element_by_id("SIGUNGU_NM0")
    element.send_keys(gu)
    
    time.sleep(2)
    
    xpath = """//*[@id="searRgSelect"]"""
    element_sel_gu = driver.find_element_by_xpath(xpath).click()
    
    time.sleep(1)
    
    xpath = """//*[@id="glopopd_excel"]"""
    element_get_excel = driver.find_element_by_xpath(xpath).click()
    
    time.sleep(1)


# In[29]:


driver.close()


# In[30]:


import pandas as pd
from glob import glob


# In[31]:


glob('../data/지역_위치별(주유소)*xls')


# In[33]:


stations_files = glob('../data/지역_위치별(주유소)*xls')
stations_files


# In[34]:


tmp_raw = []

for file_name in stations_files:
    tmp = pd.read_excel(file_name, header=2)
    tmp_raw.append(tmp)
    
station_raw = pd.concat(tmp_raw)


# In[35]:


station_raw.head()


# In[36]:


station_raw.info()


# In[37]:


stations = pd.DataFrame({'Oil_store':station_raw['상호'], 
                                       '주소':station_raw['주소'],
                                       '가격':station_raw['휘발유'],
                                       '셀프':station_raw['셀프여부'],
                                       '상표':station_raw['상표']  })
stations.head()


# In[38]:


stations['구'] = [eachAddress.split()[1] for eachAddress in stations['주소']]
stations.head()


# In[39]:


stations[stations['가격']=='-']


# In[40]:


stations = stations[stations['가격'] != '-']
stations.head()


# In[41]:


stations.info()


# In[42]:


stations['가격'] = [float(value) for value in stations['가격']]


# In[43]:


stations.reset_index(inplace=True)
del stations['index']


# In[44]:


stations.info()


# In[45]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

import platform

path = "c:/Windows/Fonts/malgun.ttf"
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~') 


# In[46]:


stations.boxplot(column='가격', by='셀프', figsize=(12,8));


# In[47]:


plt.figure(figsize=(12,8))
sns.boxplot(x="상표", y="가격", hue="셀프", data=stations, palette="Set3")
plt.show()


# In[51]:


stations.sort_values(by='가격', ascending=True).head(10)


# In[ ]:





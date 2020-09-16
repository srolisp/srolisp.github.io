#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


crime_anal_police = pd.read_csv('../data/02. crime_in_Seoul.csv', thousands=',', 
                                encoding='euc-kr')
crime_anal_police.head()


# In[3]:


crime_anal_police


# In[4]:


get_ipython().system('pip install googlemaps')


# In[5]:


import googlemaps


# In[6]:


gmaps_key = "AIzaSyC7OAswWavpZm4T_a4I6KWkgSOZ4wxGILI" # 자신의 key를 사용합니다.
gmaps = googlemaps.Client(key=gmaps_key)


# In[7]:


gmaps.geocode('서울중부경찰서', language='ko')


# In[8]:


crime_anal_police['관서명']


# In[9]:


a="중부서"


# In[10]:


str(a[:-1])


# In[11]:


station_name = []

for name in crime_anal_police['관서명']:
    station_name.append('서울' + str(name[:-1]) + '경찰서')

station_name


# In[12]:


station_addreess = []
station_lat = []
station_lng = []


# In[13]:


tmp = gmaps.geocode("서울중부경찰서", language='ko')
tmp[0]


# In[14]:


for name in station_name:
    tmp = gmaps.geocode(name, language='ko')
    station_addreess.append(tmp[0].get("formatted_address"))
    
    tmp_loc = tmp[0].get("geometry")

    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    
    print(name + '-->' + tmp[0].get("formatted_address"))


# In[15]:


station_addreess


# In[16]:


station_lat


# In[18]:


station_lng


# In[19]:


gu_name = []


# In[20]:


name='대한민국 서울특별시 중구 을지로동 수표로 27'


# In[21]:


tmp = name.split()


# In[22]:


tmp


# In[23]:


tmp_gu1 = [gu for gu in tmp if gu[-1] == '구'][0]


# In[24]:


tmp_gu1


# In[25]:


crime_anal_police


# In[26]:


gu_name = []

for name in station_addreess:
    tmp = name.split()
    
    tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
    
    gu_name.append(tmp_gu)
    
crime_anal_police['구별'] = gu_name
crime_anal_police.head()


# In[27]:


crime_anal_police[crime_anal_police['관서명']=='금천서']


# In[28]:


crime_anal_police.loc[crime_anal_police['관서명']=='금천서', ['구별']] = '금천구'
crime_anal_police[crime_anal_police['관서명']=='금천서']


# In[29]:


crime_anal_police.to_csv('../data/02. crime_in_Seoul_include_gu_name.csv',
                         sep=',', encoding='utf-8')


# In[30]:


crime_anal_police.head()


# In[31]:


crime_anal_raw = pd.read_csv('../data/02. crime_in_Seoul_include_gu_name.csv', 
                             encoding='utf-8')
crime_anal_raw.head()


# In[32]:


crime_anal_raw = pd.read_csv('../data/02. crime_in_Seoul_include_gu_name.csv', 
                             encoding='utf-8', index_col=0)

crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)
crime_anal.head()


# In[ ]:





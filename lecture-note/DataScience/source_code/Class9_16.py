#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


crime_anal_police = pd.read_csv('../data/02. crime_in_Seoul.csv', thousands=',', 
                                encoding='euc-kr')
crime_anal_police.head()


# In[4]:


crime_anal_police


# In[5]:


get_ipython().system('pip install googlemaps')


# In[6]:


import googlemaps


# In[7]:


gmaps_key = "AIzaSyC7OAswWavpZm4T_a4I6KWkgSOZ4wxGILI" # 자신의 key를 사용합니다.
gmaps = googlemaps.Client(key=gmaps_key)


# In[8]:


gmaps.geocode('서울중부경찰서', language='ko')


# In[9]:


crime_anal_police['관서명']


# In[10]:


a="중부서"


# In[11]:


str(a[:-1])


# In[12]:


station_name = []

for name in crime_anal_police['관서명']:
    station_name.append('서울' + str(name[:-1]) + '경찰서')

station_name


# In[13]:


station_addreess = []
station_lat = []
station_lng = []


# In[14]:


tmp = gmaps.geocode("서울중부경찰서", language='ko')
tmp[0]


# In[15]:


for name in station_name:
    tmp = gmaps.geocode(name, language='ko')
    station_addreess.append(tmp[0].get("formatted_address"))
    
    tmp_loc = tmp[0].get("geometry")

    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    
    print(name + '-->' + tmp[0].get("formatted_address"))


# In[16]:


station_addreess


# In[17]:


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


# In[33]:


crime_anal_raw = pd.read_csv('../data/02. crime_in_Seoul_include_gu_name.csv', 
                             encoding='utf-8', index_col=0)

crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)
crime_anal.head()


# In[34]:


crime_anal['강간검거율'] = crime_anal['강간 검거']/crime_anal['강간 발생']*100
crime_anal['강도검거율'] = crime_anal['강도 검거']/crime_anal['강도 발생']*100
crime_anal['살인검거율'] = crime_anal['살인 검거']/crime_anal['살인 발생']*100
crime_anal['절도검거율'] = crime_anal['절도 검거']/crime_anal['절도 발생']*100
crime_anal['폭력검거율'] = crime_anal['폭력 검거']/crime_anal['폭력 발생']*100

del crime_anal['강간 검거']
del crime_anal['강도 검거']
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

crime_anal.head()


# In[35]:


con_list = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

for column in con_list:
    crime_anal.loc[crime_anal[column] > 100, column] = 100
    
crime_anal.head()


# In[36]:


crime_anal.rename(columns = {'강간 발생':'강간', 
                             '강도 발생':'강도', 
                             '살인 발생':'살인', 
                             '절도 발생':'절도', 
                             '폭력 발생':'폭력'}, inplace=True)
crime_anal.head()


# In[37]:


get_ipython().system('pip install scikit-learn')


# In[38]:


from sklearn import preprocessing

col = ['강간', '강도', '살인', '절도', '폭력']

x = crime_anal[col].values
min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x.astype(float))
crime_anal_norm = pd.DataFrame(x_scaled, columns = col, index = crime_anal.index)

col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
crime_anal_norm[col2] = crime_anal[col2]
crime_anal_norm.head()


# In[39]:


result_CCTV = pd.read_csv('../data/01. CCTV_result.csv', encoding='UTF-8', 
                          index_col='구별')
crime_anal_norm[['인구수', 'CCTV']] = result_CCTV[['인구수', '소계']]
crime_anal_norm.head()


# In[40]:


col = ['강간','강도','살인','절도','폭력']
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis=1)
#=a+b+c+e
crime_anal_norm.head()


# In[41]:


col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm['검거'] = np.sum(crime_anal_norm[col], axis=1)
crime_anal_norm.head()


# In[42]:


crime_anal_norm


# In[ ]:





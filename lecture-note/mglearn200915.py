import pandas as pd
df1 = pd.DataFrame({'A' : ['A0', 'A1', 'A2', 'A3'],
                    'B' : ['B0', 'B1', 'B2', 'B3'],
                    'C' : ['C0', 'C1', 'C2', 'C3'],
                    'D' : ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A' : ['A4', 'A5', 'A2', 'A3'],
                    'B' : ['B4', 'B5', 'B2', 'B3'],
                    'C' : ['C4', 'C5', 'C2', 'C3'],
                    'D' : ['D4', 'D5', 'D2', 'D3']},
                   index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A' : ['A8', 'A9', 'A10', 'A11'],
                    'B' : ['B8', 'B9', 'B10', 'B11'],
                    'C' : ['C8', 'C9', 'C10', 'C11'],
                    'D' : ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

result = pd.concat([df1, df2, df3])
print(result)

df4 = pd.DataFrame({'B' : ['B2', 'B3', 'B6', 'B7'],
                    'D' : ['C2', 'C3', 'C6', 'C7'],
                    'F' : ['D2', 'D3', 'D6', 'D7']},
                   index=[2, 3, 6, 7])

result = pd.concat([df1, df4], axis=1)
print(result)

result = pd.concat([df1, df4], axis=1, join='inner')
print(result)

left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                      'A': ['A0', 'A1', 'A2', 'A3'],
                      'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

result = pd.concat([left, right], axis=1)
print(result)

result = pd.merge(left, right, on='key')
print(result)

import matplotlib.pyplot as plt
%matplotlib inline 

plt.figure()                    # 빈창을 그려라
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()

import numpy as np
t = np.arange(0,12,0.01)        # 0~12범위를 0.01 단위로

y = np.sin(t)

plt.figure(figsize=(10,6)) # 세로 10칸 가로 6칸 대충 그렇다
plt.plot(t, y)
plt.grid()                      # 격자를 넣는다 인치단위라고 한다.
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, y)
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, y)
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t))
plt.plot(t, np.cos(t))
plt.grid()
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), label='sin')
plt.plot(t, np.cos(t), label='cos')
plt.grid()
plt.legend()                    # 범례추가 (위에 라벨 설정)
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), lw=3, label='sin') # lw는 선두께
plt.plot(t, np.cos(t), 'r', label='cos')  # 선 색깔을 red로
plt.grid()
plt.legend()   
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(t, np.sin(t), lw=3, label='sin') # lw는 선두께
plt.plot(t, np.cos(t), 'r', label='cos')  # 선 색깔을 red로
plt.grid()
plt.legend()   
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.title('Example of sinewave')
plt.show()

t = np.arange(0, 5, 0.5)
plt.figure(figsize=(10,6))
plt.plot(t, t, 'r--')           # red, dash
plt.plot(t, t**2, 'bs')
plt.plot(t, t**3, 'g')        # g< g> g^ 삼각형 방향 바꾸기
plt.show()

t = [0, 1, 2, 3, 4, 5, 6]
y = [1, 4, 5, 8, 9, 5, 3]

plt.figure(figsize=(10,6))
plt.plot(t, y, color='green', linestyle='dashed', marker='o', markerfacecolor='red', markersize=12)  # linestyle, marker 모양,색상,크기
plt.grid()
plt.show()

t = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 8, 7, 9, 8, 3, 2, 4, 3, 4])
plt.figure(figsize=(10,6))
plt.scatter(t, y, marker='^')
plt.show()

s1 = np.random.normal(loc=0, scale=1, size=1000) # 0이 평균 편차1 사이즈1000
s2 = np.random.normal(loc=5, scale=0.5, size=1000)
s3 = np.random.normal(loc=10, scale=2, size=1000)

plt.figure(figsize=(10,6))
plt.plot(s1, label='s1')
plt.plot(s2, label='s2')
plt.plot(s3, label='s3')
plt.legend()
plt.show()

plt.boxplot((s1, s2, s3))       # 정보를 많이 전달해줌. 주황색은 중위값을 의미
plt.grid()
plt.show()

import pandas as pd
CCTV_Seoul = pd.read_excel('DataScience/data/aaaa.xlsx', thousands=',')
CCTV_Seoul.head(25)

name_split =CCTV_Seoul["기관명"].str.split(" ")
name_split

CCTV_Seoul['기관명'] = name_split.str.join(sep='')
CCTV_Seoul.tail(20)

CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]: '구별'}, inplace=True)
CCTV_Seoul.head()

pop_Seoul=pd.read_csv('DataScience/data/report.txt', sep='\t')
pop_Seoul.head()

pop_Seoul=pd.read_csv('DataScience/data/report.txt', sep='\t', header=2, thousands=',')
pop_Seoul

pop_Seoul=pop_Seoul[['자치구','계', '계.1', '계.2', '65세이상고령자']]
pop_Seoul

pop_Seoul.drop([0], inplace=True)
pop_Seoul.head()

pop_Seoul.rename(columns={pop_Seoul.columns[0]:'구별',
pop_Seoul.columns[1]:'인구수',pop_Seoul.columns[2]:'한국인',pop_Seoul.columns[3]:'외국인',pop_Seoul.columns[4]:'고령자'}, inplace=True)

pop_Seoul.head(30)

CCTV_Seoul.sort_values(by='소계', ascending=False).head(5)

CCTV_Seoul['최근증가율']=(CCTV_Seoul['2018년']+CCTV_Seoul['2017년']+CCTV_Seoul['2016년']+CCTV_Seoul['2015년']+CCTV_Seoul['2014년'])/(CCTV_Seoul['2013년']+CCTV_Seoul['2012년']+CCTV_Seoul['2011년 이전'])*100
CCTV_Seoul['최근증가율']

CCTV_Seoul.sort_values(by='최근증가율', ascending=False).head(5)

pop_Seoul['구별'].unique()

CCTV_Seoul['구별'].unique()

CCTV_Seoul[CCTV_Seoul['구별'].isnull()]

CCTV_Seoul

CCTV_Seoul.drop([10], inplace=True)

CCTV_Seoul[CCTV_Seoul['구별'].isnull()]

CCTV_Seoul

CCTV_Seoul.drop([24], inplace=True)

CCTV_Seoul[CCTV_Seoul['구별'].isnull()]

pop_Seoul

pop_Seoul['외국인비율']=pop_Seoul['외국인']/pop_Seoul['인구수']*100
pop_Seoul['고령자비율']=pop_Seoul['고령자']/pop_Seoul['인구수']*100
pop_Seoul.head()

pop_Seoul.sort_values(['고령자비율'], ascending=False).head(10)

print(CCTV_Seoul)

data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
data_result.head(23)

del data_result['2011년 이전']
del data_result['2012년']
del data_result['2013년']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
del data_result['2017년']
del data_result['2018년']

data_result.head()

data_result.set_index('구별', inplace=True)
data_result.head()

import numpy as np
np.corrcoef(data_result['고령자비율'], data_result['소계'])

np.corrcoef(data_result['외국인비율'], data_result['소계'])

np.corrcoef(data_result['인구수'], data_result['소계'])

data_result

# import matplotlib.pyplot as plt
# %matplotlib inline

# import platform

# from matplotlib import font_manager, rc(plt.rcParams['axes.unicode_minus'] = False

plt.figure()
data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))
plt.show()

data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
plt.show()

data_result.head()

data_result['CCTV비율'] = data_result['소계'] / data_result['인구수'] * 100
data_result.head()

data_result['CCTV비율'].sort_values().plot(kind='barh', grid=True, figsize=(10,6))
plt.show()

plt.figure(figsize=(6,6))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
fp1

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

plt.figure(figsize=(10,10))
plt.scatter(data_result['인구수'], data_result['소계'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV')
plt.grid()
plt.show()

fp1 = np.polyfit(data_result['인구수'], data_result['소계'], 1)
f1 = np.poly1d(fp1)
fx = np.linspace(100000, 600000, 100)

data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구수']))

df_sort = data_result.sort_values(by='오차', ascending=False)
df_sort.head()

plt.figure(figsize=(14, 10))
plt.scatter(data_result['인구수'], data_result['소계'], c=data_result['오차'], s=50)
plt.colorbar()
plt.grid()
plt.show()

plt.figure(figsize=(14, 10))
plt.scatter(data_result['인구수'], data_result['소계'], c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
for n in range(10):
  # 점선 약간 옆에 인덱스 네임을 보여주려고..
  plt.text(df_sort['인구수'][n]*1.02, df_sort['소계'][n]*0.98, df_sort.index[n], fontsize=15) 
plt.xlabel('인구수')
plt.ylabel('인구당비율')
plt.colorbar()
plt.grid()
plt.show()

import numpy as np
import pandas as pd
crime_anal_police=pd.read_csv('DataScience/data/crimeSeoul.csv', thousands=',', encoding='euc-kr')

print(crime_anal_police)

import googlemaps

gmaps_key = 'AIzaSyCr3vC-BgvsbGGdbfB6wJsQOt1fFyV-09E'
gmaps = googlemaps.Client(key=gmaps_key)
print(gmaps)

gmaps.geocode('서울중부경찰서', language='ko')

print(crime_anal_police['관서명'])

a = "중부서"
print(str(a[:-1]))

station_name = []
for name in crime_anal_police['관서명']:
  station_name.append('서울' + str(name[:-1]) + '경찰서')

print(station_name)

tmp = gmaps.geocode("서울중부경찰서", language='ko')
print(tmp)

print(tmp[0]['formatted_address'])

station_address = []
station_lat = []
station_lng = []
for name in station_name:
  tmp = gmaps.geocode(name, language='ko')
  station_address.append(tmp[0].get('formatted_address'))

  tmp_loc = tmp[0].get('geometry')
  station_lat.append(tmp_loc['location']['lat'])
  station_lng.append(tmp_loc['location']['lng'])

  print(name + '-->' + tmp[0].get('formatted_address'))

print(station_lat)

print(station_lng)

print(station_address)

gu_name = []

name = '대한민국 서울특별시 중구 을지로동 수표로 27'

tmp = name.split()
print(tmp)

# print(tmp[2])
tmp_gu1 = [gu for gu in tmp if gu[-1] == '구']
print(tmp_gu1)

print(crime_anal_police)

gu_name = []

for name in station_address:
  tmp = name.split()

  tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]

  gu_name.append(tmp_gu)
crime_anal_police['구별'] = gu_name
print(crime_anal_police)

print(crime_anal_police[crime_anal_police['관서명']=='금천서'])

print(crime_anal_police.loc[crime_anal_police['관서명']=='금천서', ['구별']])

# print(crime_anal_police.loc[crime_anal_police['관서명']=='금천서', ['구별']] = '금천구')
print(crime_anal_police[crime_anal_police['관서명']=='금천서'])

crime_anal_police.to_csv('data/200915-crime-in-seoul_include_gu_name.csv', sep=',', encoding='utf-8')

print(crime_anal_police.head())

crime_anal_raw = pd.read_csv('data/200915-crime-in-seoul_include_gu_name.csv', encoding='utf-8', index_col=0)
print(crime_anal_raw)

crime_anal = pd.pivot_table(crime_anal_raw, index='구별', aggfunc=np.sum)
print(crime_anal)

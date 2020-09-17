import matplotlib.pyplot as plt
%matplotlib inline

import seaborn as sns
import numpy as np

x = np.linspace(0, 14, 100)
y1 = np.sin(x)
y2 = 2*np.sin(x+0.5)
y3 = 3*np.sin(x+1.0)
y4 = 4*np.sin(x+1.5)

plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)
plt.show()

sns.set_style('white')

plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)

plt.show()

sns.set_style('dark')

plt.figure(figsize=(10,6))
plt.plot(x,y1, x,y2, x,y3, x,y4)

plt.show()

sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')

tips=sns.load_dataset('tips')
tips.head()

plt.figure(figsize=(8,6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()

plt.figure(figsize=(8,6))
sns.boxplot(x='day', y='total_bill', hue='smoker', data=tips, palette='Set3')
plt.show()

sns.set_style("darkgrid")
sns.lmplot(x='total_bill', y='tip', data=tips, height=7)
plt.show()

sns.set_style("darkgrid")
sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips, height=7)
plt.show()

sns.set_style("darkgrid")
sns.lmplot(x='total_bill', y='tip', hue='day', data=tips, height=7)
plt.show()

uniform_data = np.random.rand(10, 12)
uniform_data

sns.heatmap(uniform_data)
plt.show()

sns.set(style='ticks')
iris = sns.load_dataset('iris')
print(iris.head())

sns.pairplot(iris, hue='species')
plt.show()

import folium
m = folium.Map(location=[45.5236, -122.6750])
m

import folium
m = folium.Map(location=[45.5236, -122.6750])
m

m.__dir__()

m._to_png()

import os
os.get_exec_path()

m._to_png(5)

import io
import folium
from PIL import Image

def folium_map_to_png (m):
  img_data = m._to_png(1)
  img = Image.open(io.BytesIO(img_data))
  return img

import io
import folium
from PIL import Image

m = folium.Map(location=[45.5236, -122.6750], width=500, height=300)
# img_data = m._to_png(5)
# img = Image.open(io.BytesIO(img_data))

def folium_map_to_png (m):
  img_data = m._to_png(1)
  img = Image.open(io.BytesIO(img_data))
  return img
folium_map_to_png(m)

map_osm = folium.Map(location=[45, -122])
folium_map_to_png(map_osm)

map_osm = folium.Map(location=[45, -122], tiles='stamen toner', zoom_start=13, width=300, height=200)
folium_map_to_png(map_osm)

map_osm = folium.Map(location=[45, -122], # tiles='stamen toner', 
                     zoom_start=8, width=500, height=300)

folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows', icon=folium.Icon(icon='cloud')).add_to(map_osm)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge', icon=folium.Icon(icon='cloud')).add_to(map_osm)

folium_map_to_png(map_osm)

map_1 = folium.Map(location=[45.372, -121.6972], zoom_start=12, 
                   tiles='Stamen Terrain')
folium.Marker([45.3288, -121.6625], popup='Mt. Hood Meadows', 
              icon=folium.Icon(color='blue',icon='cloud')).add_to(map_1)
folium.Marker([45.3311, -121.7113], popup='Timberline Lodge', 
              icon=folium.Icon(color='green')).add_to(map_1)
folium.Marker([45.3300, -121.6823], popup='Some Other Location', 
              icon=folium.Icon(color='red',icon='info-sign')).add_to(map_1)
folium_map_to_png(map_1)

map_2 = folium.Map(location=[45.5236, -122.6750], tiles='Stamen Toner', 
                   zoom_start=13)
folium.Marker([45.5244, -122.6699], popup='The Waterfront' ).add_to(map_2)
folium.CircleMarker([45.5215, -122.6261], radius=30, 
                    popup='Laurelhurst Park', color='red', 
                    fill_color='green', ).add_to(map_2)
folium_map_to_png(map_2)

map_5 = folium.Map(location=[45.5236, -122.6750], zoom_start=13)
folium.RegularPolygonMarker([45.5012, -122.6655], 
                            popup='Ross Island Bridge', fill_color='#132b5e', 
                            number_of_sides=3, radius=10).add_to(map_5)
folium.RegularPolygonMarker([45.5132, -122.6708], 
                            popup='Hawthorne Bridge', fill_color='#45647d', 
                            number_of_sides=4, radius=10).add_to(map_5)
folium.RegularPolygonMarker([45.5275, -122.6692], 
                            popup='Steel Bridge', fill_color='#769d96', 
                            number_of_sides=6, radius=10).add_to(map_5)
folium.RegularPolygonMarker([45.5318, -122.6745], 
                            popup='Broadway Bridge', fill_color='#769d96', 
                            number_of_sides=8, radius=10).add_to(map_5)
folium_map_to_png(map_5)

state_unemployment = '~/pg/2020/python/uiap/lecture-note/DataScience/data/02-folium_US_Unemployment_Oct2012.csv'

state_data = pd.read_csv(state_unemployment)
state_data.head()

state_geo = '/Users/sroh/pg/2020/python/uiap/lecture-note/DataScience/data/02-folium_us-states.json'

map = folium.Map(location=[40, -98], zoom_start=4)
map.choropleth(geo_data=state_geo, data=state_data,
             columns=['State', 'Unemployment'],
             key_on='feature.id',
             fill_color='YlGn',
             legend_name='Unemployment Rate (%)')
folium_map_to_png(map)

# gmaps_key = 'AIzaSyCr3vC-BgvsbGGdbfB6wJsQOt1fFyV-09E'
import numpy as np
import pandas as pd

crime_anal_police = pd.read_csv('data/200915-crime-in-seoul_include_gu_name.csv', encoding='utf-8')
print(crime_anal_police)

crime_anal_police = pd.read_csv('data/200915-crime-in-seoul_include_gu_name.csv', encoding='utf-8', index_col=0)
print(crime_anal_police)

crime_anal = pd.pivot_table(crime_anal_police, index='구별', aggfunc=np.sum)
print(crime_anal)

crime_anal['강간검거율'] = crime_anal['강간 검거'] / crime_anal['강간 발생'] * 100
crime_anal['강도검거율'] = crime_anal['강도 검거'] / crime_anal['강도 발생'] * 100
crime_anal['살인검거율'] = crime_anal['살인 검거'] / crime_anal['살인 발생'] * 100
crime_anal['절도검거율'] = crime_anal['절도 검거'] / crime_anal['절도 발생'] * 100
crime_anal['폭력검거율'] = crime_anal['폭력 검거'] / crime_anal['폭력 발생'] * 100

del crime_anal['강간 검거'] 
del crime_anal['강도 검거'] 
del crime_anal['살인 검거']
del crime_anal['절도 검거']
del crime_anal['폭력 검거']

print(crime_anal)

con_list = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

for column in con_list:
  crime_anal.loc[crime_anal[column] > 100, column] = 100
print(crime_anal)

crime_anal.rename(columns = {'강간 발생':'강간', 
                             '강도 발생':'강도', 
                             '살인 발생':'살인', 
                             '절도 발생':'절도', 
                             '폭력 발생':'폭력'}, inplace=True)
print(crime_anal.head())

from sklearn import preprocessing

col = ['강간', '강도', '살인', '절도', '폭력']

x = crime_anal[col].values
min_max_scaler = preprocessing.MinMaxScaler()

x_scaled = min_max_scaler.fit_transform(x.astype(float))
crime_anal_norm = pd.DataFrame(x_scaled, columns = col, index = crime_anal.index)

col2 = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']
crime_anal_norm[col2] = crime_anal[col2]
print(crime_anal_norm.head())

result_CCTV = pd.read_csv('DataScience/data/01. CCTV_result.csv', encoding='UTF-8', 
                          index_col='구별')
crime_anal_norm[['인구수', 'CCTV']] = result_CCTV[['인구수', '소계']]
print(crime_anal_norm.head())

col = ['강간','강도','살인','절도','폭력']
crime_anal_norm['범죄'] = np.sum(crime_anal_norm[col], axis=1)
#=a+b+c+e
print(crime_anal_norm.head())

col = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_anal_norm['검거'] = np.sum(crime_anal_norm[col], axis=1)
crime_anal_norm.head()

print(crime_anal_norm)

import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().run_line_magic('matplotlib', 'inline')

sns.pairplot(crime_anal_norm, vars=["강도", "살인", "폭력"], kind='reg', height=3)
plt.show()

sns.pairplot(crime_anal_norm, vars=["강도", "살인", "폭력"], kind='reg', height=3)
plt.show()

sns.pairplot(crime_anal_norm, x_vars=["인구수", "CCTV"], 
             y_vars=["살인검거율", "폭력검거율"], kind='reg', height=3)
plt.show()

tmp_max = crime_anal_norm['검거'].max()
crime_anal_norm['검거'] = crime_anal_norm['검거'] / tmp_max * 100
crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거', ascending=False)
print(crime_anal_norm_sort)

target_col = ['강간검거율', '강도검거율', '살인검거율', '절도검거율', '폭력검거율']

crime_anal_norm_sort = crime_anal_norm.sort_values(by='검거', ascending=False)

plt.figure(figsize = (10,10))
sns.heatmap(crime_anal_norm_sort[target_col], annot=True, fmt='f', 
                    linewidths=.5, cmap='RdPu')
plt.title('범죄 검거 비율 (정규화된 검거의 합으로 정렬)')
plt.show()

crime_anal_norm.to_csv('data/200916-crime-in-seoul_final.csv', sep=',', 
                       encoding='utf-8')

import folium
import json

geo_path = './Datascience/data/02-skorea_municipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))

map = folium.Map(location=[37.5502, 126.982], zoom_start=11, 
                 tiles='Stamen Terrain')

map.choropleth(geo_data = geo_str,
               data = crime_anal_norm['범죄'],
               columns = [crime_anal_norm.index, crime_anal_norm['범죄']],
               fill_color = 'PuRd', #PuRd, YlGnBu
               key_on = 'feature.id')
folium_map_to_png(map)

from selenium import webdriver
driver = webdriver.Chrome('/Users/sroh/Downloads/chromedriver')
# http://www.opinet.co.kr/searRgSelect.do
# http://www.opinet.co.kr/user/main/mainView.do
driver.get("http://www.opinet.co.kr/searRgSelect.do")

import os
os.get_exec_path()



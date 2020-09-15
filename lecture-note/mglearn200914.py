import pandas as pd
import numpy as np

s=pd.Series([1,3,5,np.nan, 6,8])
s

dates = pd.date_range('20200722', periods=6)
dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df

df = pd.DataFrame([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [7, 55, 4, 2], [3, 5, 6, 2], [2, 3, 4, 4]], index=dates, columns=['A', 'B', 'C', 'D'])
df

df.index

df.columns

df.values

df.info

df.info()

df.describe()

df['A']

df[0:3]

df[2:5]

df['20200723':'20200726']

dates

df.loc[dates[0]]

df.loc[:, ['A', 'B']]

df.loc[:, ['A', 'B']]

df.loc[:, 'A' : 'C']

df.loc['20200723' : '20200726', 'B' : 'C']

df.iloc[3:5, 0:2]

df.iloc[[1, 2, 4], [0, 2]]

df[df['A']>0]

df[df>0]

# df2=df.copy() 복사하려면 이렇게..
df2=pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df2

df2['E'] = ['one', 'two', 'three', 'four', 'five', 'six']
df2

df2['E'].isin(['two', 'four'])

df2[df2['E'].isin(['two', 'four'])]

df2

df2 = df2.iloc[:, :4]

df2.apply(lambda x: x.max() - x.min())

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

CCTV_Seoul

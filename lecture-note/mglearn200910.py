# 데이터프레임을 이용하기 위하여 pandas 패키지를 임포트한다.
import pandas as pd
# 구글에서 받은 타이타닉호 관련 데이터를 읽어들인다.
df_train = pd.read_excel('./data/titanic3.xls')
df_train.head(10)

df_train.columns

df_train.tail(3)

df_train.info()

df_train.describe()

df_train.isnull().sum()

df_train['cabin'] = df_train['cabin'].fillna('N')
df_train['cabin']

df_train['age'] = df_train['age'].fillna(df_train['age'].mean())
df_train['age']

df_train['embarked'] = df_train['embarked'].fillna('S')

df_train_modified = df_train.drop(['boat'], axis='columns', inplace=False)
df_train_modified.drop(['body'], axis='columns', inplace=True)
df_train_modified.drop(['home.dest'], axis='columns', inplace=True)

df_train_modified['fare'] = df_train_modified['fare'].fillna(0)
df_train_modified.head()

df_train_modified['cabin'] = df_train_modified['cabin'].apply(lambda x: x[0])
df_train_modified['cabin'].value_counts()

df_train_modified['sex'].value_counts()

df_train_modified['embarked'].value_counts()

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
sns.set_palette(sns.color_palette('Set2', 10))

sns.catplot(x='sex', kind='count', data=df_train_modified)

sns.catplot(x='pclass', kind='count', data=df_train_modified)

df_train_modified['age'].hist()

sns.catplot(x='cabin', kind='count', data=df_train_modified)

sns.catplot(x='cabin', kind='count', data=df_train_modified[df_train_modified['cabin']!='N'])

sns.catplot(x='embarked', kind='count', data=df_train_modified)

sns.catplot(x='survived', kind='count', hue='sex', data=df_train_modified)

sns.catplot(x='pclass', kind='count', hue='survived', data=df_train_modified)

sns.catplot(x='sex', kind='count', hue='survived', data=df_train_modified)

sns.distplot(df_train_modified['age'][df_train_modified['sex']=='male'])

sns.displot(df_train_modified['age'][df_train_modified['sex']=='female'])

sns.lmplot('age', 'survived', hue='sex', data=df_train_modified)

sns.catplot(x='age', kind='count', hue='survived', data=df_train_modified)

sns.catplot(x='age', kind='count', hue='survived', data=df_train_modified[df_train_modified['age'] < 6])

sns.catplot(x='age', kind='count', hue='survived', data=df_train_modified[df_train_modified['age'] > 70])

sns.catplot(x='embarked', kind='count', hue='survived', data=df_train_modified)

sns.catplot(x='cabin', kind='count', hue='survived', data=df_train_modified)

sns.lmplot(x='sibsp', y='survived', hue='sex', data=df_train_modified)

sns.lmplot(x='parch', y='survived', hue='sex', data=df_train_modified)

df_train_modified['family_size'] = df_train_modified['sibsp'] + df_train_modified['parch']
df_train_modified.head()

df_train_modified_2 = df_train_modified[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare']]
df_train_modified_2.head(20)

df_train_modified_2['sex'] = df_train_modified_2['sex'].map({'female':0, 'male':1})
df_train_modified_2.head(10)

df_train_modified_2.info

df_train_modified_2.info()

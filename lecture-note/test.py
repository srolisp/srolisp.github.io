# 사이킷런 데이터셋에서 보스톤주택가격 데이터셋을 임포트한다.
from sklearn.datasets import load_boston
# 데이터프레임을 이용하기 위해 pandas를 임포트한다.
import pandas as pd

# 보스톤 데이터셋을 로드하여 boston에 담는다.

boston = load_boston()
# 보스턴 데이터셋을 출력한다.
print(boston)

# 데이터셋의 키값들을 출력한다.
print(boston.keys())

# 데이터셋의 설명 내용을 출력한다.
print(boston.DESCR)

print(boston.feature_names)

# 데이터셋의 데이터값을 특성이름을 이용하여 데이터프레임으로 만든다.
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df

# 데이터셋의 타겟값을 데이터프레임에 넣는다.
df['target'] = boston.target
df['target']

# 데이터프레임 처음 5개를 출력한다.
df.head()

# 데이터프레임 마지막 5개를 확인한다.
df.tail()

#데이터프레임의 모양을 출력한다.
print(df.shape)
# 데이터프레임의 기본통계 정보를 출력한다.
print(df.describe())

# 데이터프레임의 마지막 컬럼값을 카운트하여 출력한다.
print(df.iloc[:, -1].value_counts())

# 데이터값을 X-data에 할당한다.
X_data = boston.data
# 타겟값을 Y_data에 할당한다.
y_data = boston.target

# X_data 를 출력한다.
print(X_data)
# Y_data 를 출력한다.
print(y_data)

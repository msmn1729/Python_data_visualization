# -*- coding: utf-8 -*-
"""실습과제1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q1NV3Tso1tegqOsHxxKTtziJRGrx3T4a
"""

# Commented out IPython magic to ensure Python compatibility.
# Matplotlib 한글 폰트 설정
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

# %config InlineBackend.figure_format = 'retina'

!apt-get -qq -y install fonts-nanum > /dev/null

fontpath = '/usr/share/fonts/truetype/nanum/NanumBarunGothic.ttf'
font = fm.FontProperties(fname=fontpath, size=9)
plt.rc('font', family='NanumBarunGothic') 
mpl.font_manager._rebuild()

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
        name=fn, length=len(uploaded[fn])))

from google.colab import drive
drive.mount('/content/drive')

import sys, os
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#——————————————————————————————————————
f = open('2007-00326_박건열-1.txt','w')  # 수험번호와 이름 입력(출력파일 이름)
stdout = sys.stdout
sys.stdout = f

print()
print("*"*20, "파이썬프로그래밍활용 1급 실기과제-1", "*"*20)
print()
print("—수험번호 : 2007-00326   이름 : 박건열 ") # 수험번호와 이름 입력 
print()
print("*"*80)

# 1. 엑셀 파일 읽기
import sys, os
import numpy as np
import pandas as pd


df = pd.read_excel('kor_tour.xlsx')
# df
print("1. 엑셀 파일 읽기")
print(df.head(3))
print("*"*80)
print()

# 2. "국적" 컬럼이 대륙 이름인 컬럼을 제거하고 국가만 남기기
ignore_list = ['아시아주', '미주', '구주', '대양주', '아프리카주']

# 2-1. "국적" 컬럼이 대륙 이름(ignore_list)인 로우 검색하기
df.loc[df['국적'].isin(ignore_list)]

# 2-2. "국적" 컬럼이 대륙 이름인 컬럼을 제거하고 df에 저장하기
df = df.loc[~df['국적'].isin(ignore_list), :] 
print("2. 대륙이름 제거한 데이타 프레임 출력")
print(df.head(3))
print("*"*80)
print()
# df

# 3. 관광객 수가 가장 많은 국가에서 적은 수 5개의 국적을 출력
df_sort = df.sort_values(by=['관광'], ascending=False)
print("3. 관광객수가 가장 많은 국가 Top 3")
print(df_sort.head(3))
print("*"*80)
print()

# 4. 국적별 '관광객비율' 컬럼 추가 
df['관광객비율'] = (df['관광']/df['계']*100).round(1)
print("4. 관광객비율 컬럼 추가한 데이타프레임 출력")
# df
print(df.head(3))
print("*"*80)
print()

# 5. 국적별 관광객 수 그래프 그리기
# 5-1. 관광객 수가 가장 많은 국가에서 적은 수 순으로 5개를 df_top으로 저장
df_top = df.sort_values(by=['관광'], ascending=False)[:10]
print(df_top.head(5))
# df_top

# 5-2. 국적별 관광객수 그래프 
plt.figure(figsize=(10,7))
plt.rc('font', family='NanumBarunGothic')
# plt.title('국적별 관광객수 Top 10')
plt.title('국적별 관광객수 Top 10')
# plt.xlabel('국적')
# plt.ylabel('관광객수')
# x = df_top['국적']
# y = df_top['관광']
plt.xlabel('국적')
plt.ylabel('관광객수')
x = df_top['국적']
y = df_top['관광']

# plt.plot([1, 2, 3], [110, 120, 130])
plt.bar(x, y, width=0.7, color="dodgerblue")
plt.show()
# plt.grid()
plt.savefig("2007-00326_박건열-2.png") # 수험번호와 이름 입력.


print("*"*27, "실기 과제 종료", "*"*27)
f.close()    
sys.stdout = stdout


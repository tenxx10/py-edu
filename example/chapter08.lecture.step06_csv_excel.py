# 1 pandas 패키지 import

import pandas as pd
import os

#현재 작업 디렉터리 확인
print(os.getcwd())

#csv 파일 읽기
score = pd.read_csv('../chapter8/data/score.csv')
print(score.info())
print(score.head())

# 3 칼럼 추출
kor = score.kor
eng = score['eng']
mat = score['mat']
dept = score['dept']

# 과목별 최고 점수
print('max kor= ',max(kor))
print('max eng= ',max(eng))
print('max mat= ',max(mat))

# 과목별 최하 점수
print('min kor= ',min(kor))
print('min eng= ',min(eng))
print('min mat= ',min(mat))

#과목별 평균 점수

from statistics import mean

print('국어 점수 평균: ', round(mean(kor), 3))
print('영어 점수 평균: ', round(mean(eng), 3))
print('수학 점수 평균: ', round(mean(mat), 3))

dept_count = {}

for key in dept:
    dept_count[key] = dept_count.get(key, 0) + 1

print(dept_count)
print('='*30)



# excel 파일 읽기

sam = pd.ExcelFile('../chapter8/data/sam_kospi.xlsx')

#2 excel 파싱
kospi = sam.parse('sam_kospi')
print(kospi.info())

#3 칼럼 추출
high = kospi ['High']
low = kospi['Low']

# 4 평균 계산
from statistics import mean
print('high mean = ', round(mean(high),3))      #소수점 세자리수 
print('low mean = ', mean(low))

# 평균계산
print('High mean = ', high.mean())
print('Low mean = ', low.mean())









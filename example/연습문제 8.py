# 문제 1번 시작
file = open('../chapter8/data/ftest.txt', mode='r')

lines = file.readlines()
docs = []    # 문장 저장
words = []   # 단어 저장

try :
    for e in lines :
        docs.append(e.strip())
    for i in e.split() :
            words.append(i)


except Exception as h :
    print('Error', h)

finally:
    file.close()

print('문장 내용')
print(docs)
print('문장 수 :', len(docs))

print('단어 내용')
print(words)
print('단어 수 :', len(words))


# 문제 2번

import pandas as pd

# 1 file read
emp = pd.read_csv('../chapter8/data/emp.csv', encoding='utf-8')    # 애초에 read 함수라서 모드 안가져와도 됨
print(emp.info())
print(emp.head())    # 칼럼명 포함 행 가져오기 여기는 3개임

# 칼럼 추출
print('관측치 길이:', len(emp))   # 이게 뭔 말인지 모르겠다


emp
# 직원별 월급

from statistics import mean









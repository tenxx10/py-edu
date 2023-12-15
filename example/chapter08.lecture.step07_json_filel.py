# 1-1 json 인코딩
import json

user = { 'id':1234, 'name':'홍길동'}         #파이썬 딕트
print(type(user))
print(user['name'])     # 왜 리스트 안에 넣으세요?

# 1-2 json 인코딩
jsonString = json.dumps(user, ensure_ascii = False)
# ASCII 인코딩 방식 적용 안함 이게 뭔말이고

# 문자열 출력
print(jsonString)     # 처음 딕트 값 데려옴. json에 저장됨
print(type(jsonString))
# print(jsonString['name'])   #일케 하면 오류남

# 2 json 디코딩
py0bj = json.loads(jsonString)
print(type(py0bj))     #클래스 딕트로 나옴

# dict 자료 확인
print(py0bj['name'])    # 요건 또 가능함 왜?
for key in py0bj :
    print(key, ':', py0bj[key])    # 나 약간 이해가 안갈지도

print('='*30)


# json file 읽기
file = open('../chapter8/data/usagov_bitly.txt', mode='r', encoding='utf-8')
lines = file.readlines()

# json 디코딩
# file (json 문자열) -> python dict 객체
rows = [ json.loads(row) for row in lines]
print('rows :', len(rows))

# 10개 원소 출력
for row in rows [:10] :
    print(row)
    print(type(row))
file.close()

# dict -> dataFrame 변환
import pandas as pd

recode_df = pd.DataFrame(rows)
print(recode_df.info())
















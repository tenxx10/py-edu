# 1 dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300) # key랑 값이랑 쌍
print(dict)

#2 dict 생성 방법 2
person = {'name':'홍길동', 'age':'35', 'address':'서울시'}
print(person)
print(person['name'])
print( type(dic), type(person))

# 3 원소 수정, 삭제, 추가
# dict 원소 수정
person['age'] = 45
print(person)

person['name'] = '이순신'
print(person)

# dict 원소 삭제
del person['address']
print(person) # name 홍길동 age 45 이거 나옴

# dict 원소 추가
person ['pay'] = 350
print(person) # 이름 나이 페이 다 나옴


# 1 요소검사
print(person['age'])
print('age'in person) #True


# 2 요소 반복
for key in person.keys() :
    print(key)
for v in person.values() :
    print(v)

for i in person.items():
    print(i)

# 1 단어 데이터 셋
charset = ['abc', 'code', 'band','band', 'abc']
wc = {} # 빈 set

# 2 get 함수 이용 (get은 key를 이용해서 값을 반환한다!!! 근데 카운트는 누가하지?

for key in charset :
    wc[key] = wc.get(key, 0) + 1 # get 이용인데 이해안감. 왜 wc 뒤에 [] 이게 있음? +1 은 뭐임?
print(wc)
print(type(wc)) # dict 구조라서 [] 인 것 같아요. 이거 딕트객체 부분이긴 함.
























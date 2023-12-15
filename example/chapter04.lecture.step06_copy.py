
# 1 얕은 복사 : 주소복사 (내용, 주소 동일)
name = ['홍길동', '이순신', '강감찬']
print('name address=', id(name))

name2 = name # 이게 지금 주소 복사하는 거임
print ('name2 address =', id(name2))

print(name)
print(name2)

# 원본 수정
name2 [0] = '옹길옹' # 원본,사본 수정
print(name)
print(name2)  # 지금 사본 수정했는데 원본도 같이 수정됨이슈
print('/')
# 2 깊은 복사 : 내용복사 (내용 동일, 주소 다름)

import copy # import로 지금 copy모듈 불러온 거임?
name3 = copy.deepcopy(name) # deepcopy 명령어 데려옴
print(name)
print(name3)

print('name address=', id(name))
print('name address=', id(name3)) # 주소 다른 거 확인 가능

# 원본 수정
name[1] = '이순신 장군'
print(name)
print(name3) # 주소가 달라서 전혀 안바뀜 타격없음
print()
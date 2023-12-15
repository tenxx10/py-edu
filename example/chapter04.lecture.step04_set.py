# 1 중복 불가
s = {1,3,5,3,1}
print (len(s))
print(s)

# 2 요소 반복
for d in s :
    print(d, end='')

print()
print()

# 3 집합관련 함수
s2 = {3,6}
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))

print()
# 4 추가, 삭제 함수
s3 = {1,3,5}
print(s3)

s3.add(7)
print(s3)

s3.discard(3)
print(s3)

# 중복 원소를 갖는 리스트
gender = [ '남', '여', '남', '여']

# 중복 원소 제거
sgender = set(gender) # list -> set
lgender = list(sgender) # set-> list
print(lgender)

print(lgender[1])


















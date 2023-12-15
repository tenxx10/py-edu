#  1 단일 list 예
lst = [ 1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst : #반복문
    print(lst[:i])

    # 2 단일 list 색인
x = list (range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2]) # 홀수 색인
print(x[1::2]) # 1부터 시작하는 짝수 색인

# 1 단일 리스트 객체 생성
a = ['a', 'b', 'c']
print(a)

# 2 중첩 리스트 객체 생성
b = [ 10, 20 , a , 5, True, '문자열']
print(b)
print(b [0]) #10

print(b [2]) #a = a, b, c
print(b [2][0]) #a
print(b [2][1:]) # b,c

# 1 단일 리스트 객체 생성
num = ['one', 'two', 'three', 'four']
print(num)
print(len(num))

# 2 라스트 원소 추가 , 삭제, 수정, 삽입
num.append('five')
print(num)

num.remove('five')
print(num)

num [3] = 4
print(num)

num.insert(0, 'zero')
print(num)

num.pop()
print(num)

num.pop()
print(num)

num.insert(1,'six')
print(num)

num.reverse()
print(num)

num.extend(b)
print(num)

num.clear()
print(num)


# 1 리스트 결합
x = [ 1,2,3,4]
y = [1.5, 2.5]
z = x + y # new object
print(z) # x,y 합친 값

# 2 리스트 확장
x.extend(y)
print(x)

# 3 리스트 추가
x.append(y)
print(x)

#4 리스트 두배 확장
lst = [1,2,3,4]
result= lst*2

print(result)
print('/')


# 1 리스트 정렬
print(result) # [1,2,3,4,1,2,3,4] > 위에 입력해둔 result값
result.sort() # 오름차순으로 정렬
print(result) # 순서대로 정렬 11223344
result.sort(reverse=True) # 내림차순 정렬법. 기억하기
print(result) #44332211

# 2 리스트 요소 검사
import random  # random 모듈 불러오기
r = [] # 빈 리스트 만들어줌
for i in range(5) :
    r.append(random.randint(1,5))


# m = int(input('번호1입력:' ))
# k = int(input('번호2입력:' ))
#
# if m in r :
#     print('있음')
# else :
#     print('없음')
#
# if k in r:
#     print('있음')
# else:
#     print('없음')

print(r)  # 랜덤숫자 5개 나옴 1~5까지. randint 했으니까 0은 제외
print('/')


#  형식 1) 변수 = [ 실행문 for ]

x = [2,4,1,5,7]
# print(x **2 )  error!

lst = [ i ** 2 for i in x ]
print(lst) # 4, 16,1, 25,49 가 나와야겠지??

# 형식 2 ) 변수 = [ 실행문 for if ]
# 1~10 -> 2의 배수만 추출 -> i*2  -> list 저장
num = list(range(1,11))

lst2 = [ i*2 for i in num if i % 2 == 0 ]
print(lst2) # 4,8,12,16,20
















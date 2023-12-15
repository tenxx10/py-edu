# 1 카운터와 누적변수
cnt = tot = 0 # 변수 초기화
while cnt <5 : # True : loop 수행
    cnt += 1 # 카운터 변수(cnt = cnt +1)
    tot += cnt # 누적변수 : tot= tot + cnt
    print(cnt,tot)

# 실습 1~100 사이 3의 배수 합과 원소 추출하기
#* 어렵고 복잡하니까 몇번 따라쓰기
cnt = tot = 0
dataset = [] # 빈 리스트

while cnt < 100 : # 100회 반복
    cnt += 1 # 카운터
    if cnt % 3 == 0:
        tot += cnt # 누적변수
        dataset.append(cnt) # cnt 추가

print('1 ~ 100 사이 3의 배수 합 = %d'%tot)
print('dataset =', dataset)

# # 무한 루프 (loop)
# numData = []
#
# while True:
#     num = int(input("숫자입력: "))
#
#     if num % 10 == 0 : #exit 조건식
#         print("여기서 나가")
#         break
#
#     else:
#         print(num)
#         numData.append(num)  #lost 추가


# # 무한 루프 (loop)
# # 짝수를 보내는 루프문
# numData = []
#
# while True:
#     num = int(input("숫자입력: "))
#
#     if num % 2 == 0 : #exit 조건식
#         print("여기서 나가")
#         break
#
#     else:
#         print(num)
#         numData.append(num)  #lost 추가


# 1 random module 추가
import random
help (random) # 모듈 도움말

# 2 random모듈의 함수 도움말
help(random.random)

#3 0~1 사이 난수 실수
r= random.random()
print('r=', r) #r=0.3940

# 실습 난수 0.01 미만이면 종료 후 난수개수 출력
cnt = 0
while True :
    r= random.random()
    print(random.random())
    if r < 0.01 :
        break # loop exit
    else :
        cnt += 1

print('난수 개수 =', cnt)


# 1 random 모듈 관련 함수 도움말
help(random.randint)
help(random.choices) # 모집단에서 k 크기 목록 반환

#2 이름 list에 전체 이름, 특정이름 출력하기
names = [ '홍길동', '이순신', '유관순']
print(names)
print(names[2])


# 3 list에서 자료 유무 확인하기
if '이순신' in names :
    print ("이순신 있음")
else :
    print('이순신 없음')

if "박혁거세" in names :
    print ("박혁거세 있음")
else :
    print("박혁거세 없음")

# 4 난수 정수로 이름 선택하기
idx = random.randint (0,2)
print(names[idx])

#
i = 0
while i < 10 :
    i += 1
    if i == 3 :
        continue # 다음문장 skip

    if i == 6 : # 탈출 조건
        break #exit
    print( i, end=' ')

# i = 0
# while i <10 :
#     i += 1 # 카운터
#     if i == 3:
#         continue # 다음문장 skip
#
#     if i == 6 :
#         break # 탈출조건
#     print(i, end=' ')





















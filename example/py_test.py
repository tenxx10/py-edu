# # 3장 예제 다시 쳐보기
#
#
# # 조건문 점수입력, 등급 나오는 거
#
#
# # 100~85 우수, 84~70 보통, 69이하 저조
# #점수랑 등급 을 만들어놓아야하는 거 아닌가요? 아무튼 똑같이 따라서보겠다
#
# score = int(input('점수를 입력해주세요: '))
# if score >= 85 and score <= 100 :
#     print('우수')
# elif score >= 70 :
#     print('보통')
# else :
#     print('저조')
#
#
# score = int(input('점수를 입력해주세요: '))
# grade = ''
#
# if score >= 85 and score <= 100 :
#     grade = '우수'
# elif score >= 70 :
#     grade = '보통'
# else :
#     grade = '저조'
#
# print('당신의 점수는 %d이고, 등급은 %s입니다'%(score,grade))
#
#
# # 리스트 내포 예제
#
# #1 형식1 = 변수 = [실행문 for ]
# x =[ 2,4,1,5,7]
# # print (x ** 2) 이렇게하면 에러뜸
#
# lst = [ i ** 2 for i in x ]
# print(lst)
#
# # 2 형식 2 변수 = 실행문 for if
# # 1~ 10 -> 2의 배수 추출 -> i *2 -> 리스트 저장 흠 이걸 어떻게 하죠
#
# num=list(range(1,11))
# lst2 = [ i * 2 for i in num if i % 2 == 0]
# print(lst2)
#
#
# # 셋 객체 예시
# s= {1,3,5,3,1,2}
# print(len(s))
# print(s)
# # 애초에 셋 {}에 넣었기때문에 중복이 걸러지는건가?
#
# #2 요소 반복
# for d in s :
#     print(d, end='')
#
# print()
# print()
#
# # 3 집합관련 함수
# s2 = {3,6}
# print(s.union(s2))
# print(s.difference(s2))
# print(s.intersection(s2))
#
#
# s3 = {1,3,5}
# print(s3)
# s3.add(7)
# print(s3)
#
# # if 중첩문 예시
# yellow_card = 0
# foul = True
#
# if foul :
#     yellow_card += 1
#     if yellow_card == 2 :
#         print('경고 누적 퇴장')
#
#     else :
#         print('조심하세요')
# else :
#     print('주의')
#
# # for 변수 in 반복 범위 또는 대산
# for x in range(1,11) :
#     print(f'팔 벌려 뛰기 {x}회')


# range(start, stop, step) 홀수,짝수, 3의 배수 !!!!!!!!!!!
# range(1,10,2) 1 이상 10미만 2만큼 증가 = 홀수 값만 뽑아냄
# range(3,10,3) 3이상 10미만 3만큼 증가 = 3,6,9

# for y in range(3,100,3) : # 3,6,9 게임 가능 *근데 만약 3,6,9만 빼고 싶다면?



# 알고리즘 재연습
# 최댓값, 최솟값
#
# # 1 입력 자료 생성
# import random # 랜덤값불러오기
# dataset = []   # 빈 리스트 만들기
#
# for i in range(10) :
#     r = random.randint(1,101)
#     dataset.append(r)
#
#     # 리스트에 r의 값을 입력함 1~100까지 중에서 10개 고르는 거임
# print(dataset)

import random
dataset = []

for i in range(5) :
    r = random.randint(1,101)
    dataset.append(r)

print(dataset)


# 변수 초기화

vmax = vmin =0

for i in dataset :
    if vmax < i :
        vmax = i
    if vmin > i :
        vmin = i

print('max=',vmax, '\nmin=', vmin)


# 선택정렬 알고리즘 예시
# 1 오름차순 정렬
dataset = [3,5,1,2,4]
n = len(dataset)

for i in range(0,n-1) :
    for j in range(i+1, n) :
        if dataset[i] > dataset [j] :    # i가 j보다 큰 경우 : 오름차순정렬
            tmp = dataset [i]
            dataset [i] = dataset [j]
            dataset [j] = tmp    # 각회전 정렬내용
    print(dataset)

print(dataset)
print()

# 내림차순 정렬
dataset = [ 3,5,1,2,4]
n= len(dataset)    #원소 개수 있어야 for range안에 넣을 n-1이 가능해짐

for i in range(0,n-1) :
    for j in range(i+1,n) :
        if dataset [i] < dataset [j] :
            tmp = dataset [i]
            dataset [i] = dataset [j]
            dataset [j] = tmp
    print(dataset)

print(dataset)    #  최종값 출력인듯?



# 이진검색 알고리즘
dataset = [5,10,18,22,35,55,75,103]
value = int(input('검색할 값 입력:'))

low = 0   # start 위치
high = len(dataset) - 1   # end 위치, 8-1
loc = 0   # 색인저장, 찾는 위치
state = False # 상태변수

while (low<= high) :
    mid = (low+ high)    # 중앙값구하기. 평균값
    if dataset [mid] > value :    #중앙값이 큰 경우
        high = mid -1     # 위치? 라는데... 흠
    elif dataset [mid] < value :
        low = mid + 1
    else :     # 찾은 경우
        loc = mid
        state = True
        break     # 반복exit     ????

    if state:
        print('찾은 위치: %d번째'%(loc+1))
    else:
        print('찾는 값은 없습니다.')

# 이거 이상함











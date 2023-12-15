# # 문제 1
#
# #ver.1
# status1 = '상품 준비'
# status2 =  '배송 중'
# status3 =  '배송 완료'
#
# print('주문상태:',status1)
# print('주문상태:',status2)
# print('주문상태:',status3)
#
# #ver2. (직접 입력받는 경우)
# print('[상품 준비, 배송 중, 배송완료 중 택1 입력해주세요]')
#
# status = str(input('입력해주세요: '))
# print('주문상태:', status)
#
#
#
#
# # 문제 2
# import random
#
# day = random.randint(4,29)
# print("오프라인 스터디 모임 날짜는 매월",day,'일로 선정됐습니다.')
#
#
#
# # 문제 3 (획득자와 지정자 사용)
#
# num = float(input('섭씨온도를 입력해주세요:'))
#
# def mainFunc(num):
#     sub = num  # 섭씨 저장자료 생성
#
#     def getter():
#         return sub
#
#     def setter():  # 변환할 화씨
#         nonlocal sub
#         sub = sub * 9/5 + 32
#         return sub
#
# # 사실 여기서
# #     def setter(hwa) :   #변환할 화씨
# #         nonlocal sub
# #         sub = hwa

# # 이렇게 사용했었는데 적용이 안되더라구요 !! ㅠㅠ 전부 sub으로만 표시하니 헷갈리는 것 같아요...
# # 혹시 다른 식이 있다면 첨부해주시면 감사하겠습니다 :)
#
#
#     return getter, setter  # 함수 클로저 반환!
#
# getter, setter = mainFunc(num)
#
# print('섭씨온도:', getter())
# print('화씨온도:', setter())
#
#
#
# # 기본 연산자로도 해봤습니다 :)
# subC = float(input('온도값을 입력해주세요: '))
# hwaF = (subC*9/5) +32
#
# print('섭씨온도:', subC)
# print('화씨온도: ', hwaF)
#
# print()
#


# 문제 4
# # for in 반복문과 if i % 3 == 0 ? 사용
#
#
#
# num = int(input('손님. 구매수량 무조건 3의 배수만 적으세요: '))
# # 3배수 뽑는 법이 알고 싶습니다...^^
# price = 1000
# print(num)
#
#
# tot = (num // 2 + num % 2)*price
# # 공식을 도저히 모르겠어서 gpt의 힘을 얻어 2+1 구하는 공식을 얻었습니다 .. ^^
# # 근데 이것도 굉장히 잘못된듯한 ..~~
#
# var = 0
# while var < num :
#     var += 1
#     if var % 3 == 0 :
#         print('2+1 상품입니다'*(num))
#
# # 진짜 몰라서 아무거나 넣었어요......
# # for i in 사용하고 싶었는데 너무 안되길래!!!!
#
#
# print('총 가격은 %d 입니다.'%tot)
# # 어떤 방식을 사용해야할지 모르겠어요  이게 한계입니다 ㅎ_ㅠ


#1번문제
#변수 값부터 순서대로 지정해주셔야 됩니다.

status = "상품 준비"
print("주문상태 : " +status)

status = "배송 중"
print("주문상태 : " +status)

status = "배송 완료"
print("주문상태 : " +status)

#2번문제
import random
d= random.randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(d) +"일로 선정됐습니다.")
print("오프라인 스터디 모임 날짜는 매월", d, "일로 선정됐습니다.")


#3번문제
c=30 #온도변수 지정
f=(c*9/5)+32
print("섭씨 온도 : "+str(c))
print("화씨 온도 : "+str(f))

c=10 #온도변수 지정
f=(c*9/5)+32
print("섭씨 온도 : "+ str(c))
print("화씨 온도 : "+ str(f))


#4번문제
#3개 살때
p=1000 #가격
g=3 #물건갯수
tot=0 #총가격

for i in range(1, g+1) :
    print("2+1 상품입니다.")
    if i%3==0 : #3의 배수인 경우 가격을 더하지 않음
        continue # skip한다는 뜻
    tot += p

print("총 가격은 "+str(tot)+"원입니다.")

#6개 살때
p=1000
g=6
tot=0

for i in range(1, g+1) :
    print("2+1 상품입니다.")
    if i%3==0 : #3의 배수인 경우 가격을 더하지 않음
        continue
    tot += p

print("총 가격은 "+str(tot)+"원입니다.")


# 입력값받아서 하는 거!! 
p=1000
g = int(input('개수를 입력해주세요:'))
tot=0

for i in range(1, g+1) :
    print("2+1 상품입니다.")
    if i%3==0 : #3의 배수인 경우 가격을 더하지 않음
        continue
    tot += p

print("총 가격은 "+str(tot)+"원입니다.")




#
#
# # 함수 정의
# def StarCount(height):
#     h_cnt= s_cnt = 0 # 층수, 별수 변수 선언 h_cnt
#
#     while h_cnt < height :
#         h_cnt += 1 # 층수 카운터(1,2,3)
#         print('*'*h_cnt) # 별 출력
#         s_cnt += h_cnt # 별수 카운터
#     return s_cnt
# # 키보드 입력
# height=int(input('height : '))
# # start 개수 출력
# #print('start 개수 : %d', %StarCount(height))
# print('start 개수 :', StarCount(height))


def StarCount(height) :
    h_cnt = s_cnt = 0   # 초기화면서 변수 선언

    while h_cnt < height :
        h_cnt += 1
        print('*'* h_cnt)
        s_cnt += h_cnt
    return s_cnt

height = int(input('height : '))
print('start 개수 : ', StarCount(height))





# 함수 정의
def bank_account (bal) :
    balance = bal # 잔액초기화(1000)

    def getBalance(): # 잔액확인(getter)
        return balance

    def deposit (money) : #입금하기 (setter)
        nonlocal balance
        balance += money

    def withdraw (money) : # (setter)
        nonlocal balance
        if balance < money :
            print('잔액이 부족합니다.')
        else :
            balance -= money

    return getBalance, deposit, withdraw  #37 28


bal=int(input('최초 계좌의 잔액을 입력하세요 :'))
print('현재 계좌 잔액은', bal, '원 입니다.')
money=int(input('입금액을 입력하세요. :'))
print(money, '원 입금후 잔액은',money+bal, '원 입니다.')
min=int(input('출금액을 입력하세요 :'))
print(min,'원 출금 후 잔액은',money+bal-min, '원 입니다.')

# 이거 복잡하게 안하고 쉽게 하고 싶다~~~!~!!!!



# #재귀 함수 정의
# def Factorial (n):
#     if n==1 : # : 종료조건
#         return 1
#
#     else :
#         # 재귀호출
#         result = n*Factorial (n-1)
#         # 5(first)->4(5-1) -> 3(4-1) -> 2(3-1) I [1(2-1)]
#         '''
#         1. stack (5, 4, 3, 2)
#         2. 곱셈:1* [2*3*4*5]
#         '''
#         print (n, end=' ')
#         return result # 120
#
# #함수 호출
# result_fact = Factorial(5)
# print('\n팩토리얼 결과 : ', result_fact)

def Factorial(n) :
    if n == 1 : # 종료조건
        return 1
    else :
        # 재귀호출할 거임
        result = n*Factorial(n-1)       #5>4(5-1)>...2(3-1)>1(2-1)
        '''
        1. stack(5,4,3,2)
        2. 곱셈: 1*[2*3*4*5]
        '''
        print (n, end='')
        return result   # 120

# 함수호출
result_fact = Factorial(5)
print('\n팩토리얼 결과:', result_fact)


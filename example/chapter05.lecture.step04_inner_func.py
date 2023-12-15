
# 1 1급 함수
def a ():
    print('a 함수')
    def b() :
        print ('b 함수')
    return b

b = a()
b ()


# 함수 클로저
data = list(range(1,101))
def outer_func(data) :
    dataSet = data
    # inner
    def tot():
        tot_val = sum (dataSet)
        return tot_val

    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val

    return tot, avg

# 외부 함수 호출 : data 생성
tot, avg = outer_func(data)

# 내부 함수 호출
tot_val = tot()
print('tot=', tot_val)
avg_val = avg(tot_val)
print('avg=', avg_val)


# #중첩함수 생략
#
# from statistics import mean   # 평균
# from statistics import sqrt   # 제곱근
#
#
# data = [ 4,5,3.5,2.5,6.3,5.5]
#
# # 1 외부함수 : 산포도 함수
# def scattering_func(data):
#     dataSet = data
#
#     # 2 내부 함수 : 산술 평균 반환
#     def avg_func():
#         avg_val = mean(dataSet)
#         return avg_val
#     # 3 내부 함수 : 분산 반환
#     def var_func(avg) :
#         diff = [ (data-avg) ** 2 for data in dataSet]
#         print(sum (diff))
#         var_val = sum(diff) / (len(dataSet)-1)
#         return var_val
#
#     # 4 내부 함수 : 표준편차 반환
#     def std_funcs(var) :
#         std_val = sqrt(var)
#         return std_val
#     # 함수 클로저 반환
#     return avg_func, var_func, std_funcs
#
# # 5 내부 함수 호출
# print('평균: ', avg)
# print('분산: ', var(avg()))
# print('표준편차:', std(var(avg())))



# 중첩함수

from statistics import mean
from statistics import sqrt

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

# 1 외부함수 : 산포도 함수
def scattering_func(data):
    dataSet = data

    # 2 내부 함수 : 산술 평균 반환
    def avg_func():
        avg_val = mean(dataSet)
        return avg_val

    # 3 내부 함수 : 분산 반환
    def var_func():
        avg = avg_func()  # 내부 함수를 호출하여 평균 계산
        diff = [(data - avg) ** 2 for data in dataSet]
        var_val = sum(diff) / (len(dataSet) - 1)
        return var_val

    # 4 내부 함수 : 표준편차 반환
    def std_funcs():
        var = var_func()  # 내부 함수를 호출하여 분산 계산
        std_val = sqrt(var)  # 내부 함수를 호출하여 표준편차 계산
        return std_val

    avg = avg_func()  # 내부 함수 호출하여 평균 계산
    var = var_func()  # 내부 함수 호출하여 분산 계산
    std = std_funcs()  # 내부 함수 호출하여 표준편차 계산

    return avg, var, std  # 함수 클로저 반환

# 5 내부 함수 호출
avg, var, std = scattering_func(data)

print('평균: ', avg)
print('분산: ', var)
print('표준편차:', std)





# 획득자와 지정자
# 1 중첩함수 정의

def  main_func(num) :
    num_val = num
    def getter() :
        return num_val
    def setter(value) :
        nonlocal num_val
        num_val = value

    return getter, setter

# 2외부함수 호출
getter, setter = main_func(100)  # 값 지정해줌

# 3 획득자, 지정자 호출
print('num=', getter())
setter (200)
print('num=',getter())


# 1 래퍼함수
def wrap(func) :
    def decorated():
        print('방가워요!')
        func()
        print('잘가요!')
    return decorated

# 2 함수 장식자 사용
@wrap
def hello() :
    print('hi~', '홍길동')

# 3 함수 호출
hello()



# 재귀함수 정의 : 1~n 카운트
def Counter(n):
    if n == 0 :
        return 0  # 종료조건
    else :
        Counter(n-1)    #재귀호출


#2 함수 호출
print('n=0 : ', Counter(0))

# 3 함수 호출2
Counter (5)



def Counter(n):
    if n == 0:
        return 0 # 종료조건: 빈 리스트 반환
    else:
        # 재귀 호출과 결과 리스트를 병합
        return Counter(n - 1)


# 1 함수 호출
print('n=0 :', Counter(0))  # 결과 출력



# def Counter(n):
#     if n > 0:
#         Counter(n - 1)  # 재귀 호출
#     print(n)  # 숫자 출력
#
# # 함수 호출
# Counter(5)


# 재귀함수 정의 : 1~ n 누적합(1+2+3+4+5=15)

def Adder(n) :
    if n == 1 :
        return 1
    else :
        result = n + Adder(n-1)   # 재귀무한호출 adder 있으니까 누적합
        print(n, end=' ')
        return result


# 2  함수호출1
print('n=1: ', Adder(1))

print('\nn=5: ', Adder(5))























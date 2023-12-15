# 분산과 표준편차 함수

from statistics import mean, variance  #평균 ,분산
from math import sqrt     # sqrt 루트
dataset = [ 2 , 4 , 5 , 6 , 1 , 8 ]

# 1 산술 평균
def Avg (data) :
     avg = mean (data)
     return avg

print('산술평균=', Avg (dataset))

# 2 분산 / 표준편차
def var_sd (data) :
    avg = Avg (data)   #함수 호출
    # list 내포

    diff = [ (d - avg) **2 for d in data]

    var = sum(diff) / (len(data)-1)
    sd = sqrt(var)

    return var, sd

# 3 함수 호출
v, s = var_sd (dataset)
print('분산=', v)
print('표준편차=',s)


# 피타고라스 정리
def pytha (s, t) :
     a = s**2 - t**2
     b = 2 * s * t
     c = s**2 + t**2
     print("3변의 길이:", a,b,c)
pytha (2,1)
print()

# 실제 잘 쓰이진 않음 그냥 쳐본 걸로 충분하심


# 몬테카를로 시뮬레이션
import random
def coin(n) :
    result = []

    for i in range(n) :
        r = random.randint(0,1)
        if ( r == 1) :
            result.append(1)  # 앞면
        else:
            result.append(0) # 뒤


    return result

print(coin(24))


#단계2 : 몬테카를로 시뮬레이션 함수 정의
def montaCoin(n):
    cnt = 0
    for i in range(n) :
        cnt += coin(1) [0] #코인 함수 호출

    result = cnt / n #누적결과를 시행횟수로 나누는 거임
    return result

print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))











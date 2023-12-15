# 1 평균과 제곱근 모듈 import

from statistics import mean
from math import sqrt

# 산술 평균 함수


def Avg(data) :
    avg = mean(data)
    return avg

# 분산과 표준편차 함수
def var_sd(data) :
    avg = Avg(data)
    diff = [(d- avg) **2 for d in data]
    var = sum(diff) / (len(data)-1)          #sum에 전부 더해줌, 6개 원소 중에서 나눠줌 = 분산값 나옴
    sd = sqrt(var)

    return var, sd

# 프로그램 시작점
if __name__ == '__main__' :
    data = [1,3,5,7]
    print('평균=', Avg(data))
    var, sd = var_sd(data)
    print('분산=', var)
    print('표준편차=', sd)









# 문제 1.

print('사각형의 넓이와 둘레를 계산합니다.')
w = int(input('사각형의 가로 입력 :'))
h = int(input('사각형의 세로 입력: '))
print('-'*30)

class Rectangle :
    w = 0
    h = 0

    def __init__(self,w,h):
        self.w = w
        self.h = h

    def area_calc(self):
        area = self.w * self.h
        return area

    def circum_calc(self):
        circum = (self.w + self.h) * 2
        return circum

rtg = Rectangle(w,h)    # 값 넣어줘야함
area = rtg.area_calc()
print('사각형의 넓이:', rtg.area_calc())

circum = rtg.circum_calc()
print('사각형의 둘레:', rtg.circum_calc())
print('-'*30)



# 문제 2

from statistics import mean
from math import sqrt

x = [5,9,1,7,4,6]

# 산포도 클래스
class Scattering :

    def __init__(self, x) :
        self.x = x

    def var_func(self):
        avg = mean(self.x)
        diff = [ (d - avg) **2 for d in self.x]    # 요거 list상태임
        # 분산 구할차례
        self.var = sum(diff) / (len(self.x)-1)
        return self.var    # 이것도 self로 받아야하나?  이게 동적변수?

    def std_func(self):
        sd = sqrt(self.var)    # 이게 너무 어려운데
        return sd   # 얘는 왜 self 필요없음?

sct = Scattering(x)
var = sct.var_func
sd = sct.std_func

print('분산:', sct.var_func() )
print('표준편차: ', sct.std_func())



# 3 문제

class Person :
    # name = gender = age = 0
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print('이름 : %s, 성별 : %s \n나이 : %d'%(self.name,self.gender, self.age))


# 키보드 입력
name = input('이름: ')
age = int(input('나이: '))
gender = input('성별(male/female/etc): ')
print('='*30)


# 객체 생성
# p = Person(name, gender, age)
p = Person('유관순', '여자', 19)
p1 = Person('홍길동','남성',35)
p.display()
print('='*30)

p1.display()
print('='*30)
# print('이름:{}, 나이:{}, 성별:{}'.format(name,age,gender))


# 문제 4번
class Employee :
    name = 0
    pay = 0

    def __init__(self,name):
        self.name = name

class Permanent(Employee) :
    def __init__(self, name, base, bonus):
        super().__init__(name) # 부모 생성자 호출, 초기화1
        self.pay = base + bonus


class Temporary(Employee):
    def __init__(self, name, tpay, time):
        super().__init__(name) # 부모 생성자 호출, 초기화1
        self.pay = tpay * time


empType = input("고용형태 선택(정규직<p>, 임시직<t>): ")

if empType == 'p' or empType == 'P' :
    name = input('이름 : ')
    base = int(input('기본급: '))
    bonus = int(input('상여급: '))
    p = Permanent(name, base, bonus)
    print('=' * 30)

    print('고용형태 : 정규직')
    print('이름: ', p.name)
    print('급여: ', format(p.pay, '3,d'))

elif empType == 't' or empType == 'T' :
    name = input('이름 : ')
    time = int(input('작업시간: '))
    tpay = int(input('시급: '))
    t = Temporary (name, tpay, time)
    print('=' * 30)

    print('고용 형태 : 임시직')
    print('이름: ', t.name)
    print('급여: ', format(t.pay, '3,d'))

else :
    print('='*30)
    print('입력 오류')

# print('='*30)
# p1=Permanent('홍길동',200000,30000)
# print(p1)   작동 안됨

#5 문제

from chapter06.myCalcPakage.calcModule import add, sub, mul, div

x = 10
y = 5

print(f'x = {x}; y = {y}일 때')

print(f'add = {add(x, y)}')
print(f'sub = {sub(x, y)}')
print(f'mul = {mul(x, y)}')
print(f'div = {div(x, y)}')
# 사용자정의함수

# 1 인수가 없는 함수
def userFunc1() :
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1()   #함수 호출


# 인수 있는 함수
def userFunc2(x,y) :
    print('userFunc2')
    z = x + y
    print('z=', z)

userFunc2(10,20)   # 함수 호출 z=30 나와야함

# 3 return 있는 함수

# def 불러와서 tot, sub, mul, div 값을 return으로 불러올 거

def userFunc3(x,y) :
    print('[ userFunc3 ]')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot,sub,mul,div

# 리턴해도 프린트 안해서 값 출력 안됨 저장만 해둔 거임

# 실인수 : 키보드 입력
x = int(input('x 입력: '))
y = int(input('y 입력: '))
print()

t,s,m,d = userFunc3 (x,y)    # 지금 호출 당한건가
print ('tot: ', t)
print('sub: ', s)
print('mul: ', m)
print('div: ', d)
















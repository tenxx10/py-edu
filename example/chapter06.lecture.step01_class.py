# 1 함수 정의
def calc_func(a,b) :
    x = a
    y = b

    def plus() :
        p = x + y
        return p

    def minus() :
        m = x - y
        return m
    return plus, minus

p, m = calc_func(10,20)
print('plus:', p())
print('minus:', m())


# 클래스 정의
class calc_class :
    x = y= 0

    def __init__(self,a,b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p

    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(10,20)

print('plus:', obj.plus())
print('minus:', obj.minus())


# 1 멤버 변수
class Car :
    cc = 0
    door =0
    carType = None # null

    # 2 생성자
    def __init__(self, cc, door, carType):
        # 멤버변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType

    # 3 메서드
    def display(self):
        print("자동차는 %dcc이고, 문짝은 %d개, 타입은 %s"%(self.cc, self.door, self.carType))

# 4 객체 생성
car1 = Car(2000,4, '승용차')
car2 = Car(3000,5, "SUV")
car3 = Car(4500,6,"대형트럭")

# 5 멤버호출

car1.display()
car2.display()
car3.display()










# 1 부모 클래스
class Flight :

    def fly(self):
        print('날다, fly 원형 메서드')

class Airplane :
    def fly(self):
        print('비행기가 날다')

class Bird :
    def fly(self):
        print('새가 날다')

class PaperAirplane :
    def fly(self):
        print('종이 비행기가 날다')

# 객체 생성
flight = Flight()
air = Airplane()
bird = Bird()
paper = PaperAirplane()


# 다형성
flight.fly()

flight = air
flight.fly()

flight = bird
flight.fly()

flight = paper
flight.fly()




















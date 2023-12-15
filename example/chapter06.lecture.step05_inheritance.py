# 1 부모 클래스
class Super :
    # 생성자 : 동적멤버 생성
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print('name: %s, age: %d'%(self.name, self.age))

sup = Super ('부모',55)
sup.display()

# 자식 클래스
class Sub(Super) :
    gender = None

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    #4 메서드 확장
    def display(self):
        print('name: %s, age : %d, gender: %s'%(self.name, self.age, self.gender))

sub = Sub('자식', 25, '여자')
sub.display()

# 1 부모 클래스
class Parent :
    def __init__(self, name, job):    # 생성자 = 객체 + 초기화
        self.name = name
        self.job = job

    # 멤버 함수 (method)
    def display(self):
        print('name: {}, job: {}'.format(self.name, self.job))

        # 부모클래스 객체 생성
p = Parent('홍길동','회사원')
p.display()


# 2 자식 클래스
class Children (Parent) :
    gender = None

    def __init__(self, name, job, gender):
        super().__init__(name, job)       # 부모클래스 생성자 호출
        self.gender = gender             # 자식 멤버변수 초기화

    # 멤버함수 (method)
    def display(self):
        print('name:{}, job: {}, gender: {}'.format(self.name, self.job, self.gender))

chil = Children('이순신','해군 장군','남자')
chil.display()






















class DatePro :
    # 1 멤버 변수
    content = "날짜 처리 클래스"

    # 2 생성자
    def __init__(self,year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # 3 객체 메서드
    def display(self):
        print("%d-%d-%d"%(self.year, self.month, self.day))

    # 클래스 메서드 ! @classmethod 쓰는 거 cls
    @classmethod
    def date_string(cls, dateStr):    #20050506
        year = dateStr[0:4]
        month = dateStr [4:6]
        day = dateStr [6:]

        print(f"{year}년 {month}월 {day}일")

# 객체 멤버 (다 불러올 것)
date = DatePro(1995,8,6)
print(date.content)
print(date.year)
print(date.day)
date.display()


# 클래스 멤버
print(DatePro.content)
# print(DatePro.year)   #attributeEroor
DatePro.date_string('19950506')











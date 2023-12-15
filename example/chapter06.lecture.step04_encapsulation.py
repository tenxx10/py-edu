class Account :
    # 은닉 멤버변수 balance, accName, accNo
    __balance : 0
    __accName : None
    __accNo : None

    # 생성자 : 멤버변수 초기화
    def __init__(self,bal,name,no):
        self.__balance = bal # 잔액 초기화
        self.__accName = name  #예금주
        self.__accNo = no   # 계좌번호

    # 계좌 정보 확인
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    #입금하기
    def deposit(self,money):
        if money < 0 :
            print('금액확인')
            return
        self.__balance += money


    # 출금하기
    def withdraw(self,money):
        if self.__balance < money:
            print('잔액부족')
            return    # 종료
        self.__balance -= money

# object 생성
acc = Account(1000, '홍길동', '125-152-4125-41')   #생성자

#getter 호출
# acc.__balance #오류남
bal = acc.getBalance()
print('계좌정보: ', bal)

#setter 호출
acc.deposit(10000)    #만원 입금
bal = acc.getBalance()
print('계좌정보: ', bal)

acc.deposit(25000)    #2만 5천원 입금
bal = acc.getBalance()
print('계좌정보: ', bal)











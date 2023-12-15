# 서식 지정자 사용
print("나는 %d살입니다" % 20)
print("나는 %s을 좋아합니다" %"파이썬")
print("Apple은 %c로 시작해요." %"A")
print("Apple은 %c로 시작해요." %"애")
print("나는 %s살입니다" % 18)

# format 함수 사용
print("나는 {}살입니다.".format(49))
print("나는 {}색과 {}색을 좋아합니다.".format("파랑","빨강"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파랑","빨강"))
print("나는 {0}색과 {1}색을 좋아하고 특히나 {1}색을 좋아합니다".format("초록","검정"))
print("나는 {0}색과 {1}색을 좋아하고 {2}색은 좋아하지 않습니다.".format("파랑","빨강","노랑"))

#f-문자열 사용
age=10
color="검은"
print(f"나는 {age}살이며, {color}색을 좋아해요")

apple="사과"
banana="바나나"
print("빨가면", apple, "맛있으면", banana)
print(f"빨가면 apple, 맛있으면 banana")

print("{0}".format(500))
# 빈칸으로 두기, 오른족 정렬, 공간 10칸 확보
print("{0:>10}".format(500))

#빈칸으로 두기, 오른쪽 정렬, + 기호 붙이기, 공간 10칸 ㅘㄱ보
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) #음수일 때
print("{0:a>+10}".format(500))
print("{0:_<10}".format(500))

print("{0:,}".format(100000000000))
print("{0:+,}".format(100000000000))
print("{0:-,}".format(100000000000)) # 앞에 - 붙이면 안됨
print("{0:+,}".format(-100000000000))

#나누기 하기 f는 실수자료형으로 나옴
print("{0}".format(5/3))

print("{0:f}".format(5/3))

print("{0:.2f}".format(5/3))





# 사이트 비밀번호 만들기

url="http://naver.com"
pw1=url.replace("http://","")
# print(pw1) #naver.com




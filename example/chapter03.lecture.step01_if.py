# 단일 조건문 형식1

var = 10 # if 블럭에서 사용될 변수
if var >= 5 : # 조건식
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')

# print('항상 실행')
#
# # 단일조건문 형식2
# # 100~85 : '우수', 84~70 '보통', 69이하 '저조'
# score = int (input('점수 입력 : '))
# if score >= 85 and score <=100 :
#     print('우수')
# else:
#     if score >= 70 :
#         print ('보통')
#     else:
#         print('저조')
#
#
# #중첩조건문
#
# score = int(input('점수입력: '))
# grade = '' # 등급
#
# if score >= 85 and score <= 100 :
#     grade = '우수'
# elif score >= 70 :
#     grade = '보통'
# else :
#     grade='저조'
#
# print('당신의 점수는 %d점이고, 등급은 %s입니다'%(score, grade))

#삼항 조건문
# 1 일반 조건문
num = 9
result = 0

if num >= 5 :
    result = num*2

else:
    result = num +2
print('result =', result)

# 2 삼항 연산자
# 형식) 변수 = 참 if (조건문) else 거짓
result2 = num*2 if num >= 5 else num+2
print('result2=', result2) #18























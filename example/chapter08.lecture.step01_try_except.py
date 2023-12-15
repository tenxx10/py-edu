# # 1 예외발생 코드
# print('프로그램 시작 !!!')
x = [ 10,30,25.2,'num',14,51]
#
# for i in x :
#     print(i)
#     y = i**2          #예외발생
#     print('y=', y)
#
# print('프로그램 종료')


# 예외 처리 코드
print('프로그램 시작!!!')

for i in x :
    try :
        y= i ** 2
        print('i=', i, ', y=', y)
    except :
        print('숫자 아님: ', i)

print('프로그램 종료!!')

# 중첩 예외처리 예문
# 유형별 예외처리
print('\n유형별 예외처리')

try :
    div = 1000 / 2.53
    print('div= %5.2f'%(div))     #정상이라는데 이게 무슨 말이지
    div = 1000 / 0                   # 산술적 예외 1
    f = open('c:\\test.txt')         # 파일 열기 2
    num = int(input('숫자입력 : '))    # 기타 예외 3
    print('num=', num)

# 다중 예외처리 클래스

except ZeroDivisionError as e :    #division by zero
    print('정보오류 : ', e)

except FileNotFoundError as e :      #[Errno 2] No such file or directory: 'c:\\test.txt'
    print('오류정보 : ', e)

except Exception as e :
    print('오류 정보: ', e)        #invalid literal for int() with base 10: 'n' 이렇게 뜸

finally:
    print('finally 영역 - 항상 실행되는 영역')











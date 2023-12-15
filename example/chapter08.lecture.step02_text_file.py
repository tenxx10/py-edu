# # 1 현재 작업 디렉터리
import os
print('\n현재경로 : ', os.getcwd())   #D:\Pywork\workspace
#

ftest1 = ftest2 = ftest3 = None

# 2 예외처리
try:
    # 3 파일 읽기
    ftest1 = open ('data/ftest.txt', mode = 'r')
    print(ftest1.read())

    # 4 파일쓰기
    ftest2 = open('data/ftest2.txt', mode='w')
    ftest2.write('my first text~')

    # 파일쓰기 + 내용추가
    ftest3 = open('data/ftest2.txt', mode='a')
    ftest3.write('\nmy second text~')      # 파일쓰기 추가

except Exception as e:
    print('Error 발생: ', e)

# finally:
#     if ftest1:
#         ftest1.close()
#     if ftest2:
#         ftest2.close()
#     if ftest3:
#         ftest3.close()
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()

print('='*30)
print('<예제 2번>')

# 파일 읽기 관련 함수
try :
    #1 read() 전체 텍스트 자료 읽기
    ftest = open('data/ftest.txt', mode= 'r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))
    print('='*30)

    # 2 readlines() 전체 텍스트 줄 단위 읽기
    ftest = open('data/ftest.txt', mode='r')
    lines = ftest.readlines()   #list 반환
    print(lines)
    print(type(lines))
    print('문단수 :', len(lines))
# 문단수 6
    print('=' * 30)

    # 3 list 문장 추출
    docs = []
    for line in lines :
        print(line.strip())  #text만 출력
        docs.append(line.strip())

    print(docs)
    print('='*30)

    # 4 readline() 한줄 읽기
    ftest = open('data/ftest.txt', mode='r')
    line = ftest.readline()   #한줄 읽기
    print(line)
    print(type(line))


except Exception as e :
    print('Error 발생 !', e)

finally:
    ftest.close()





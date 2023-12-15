# import os
#
# # 현재 작업디렉터리 경로 확인
# os.getcwd()
# #
# # 작업디렉터리 변경   ('chapter8'로 변경예정)
# os.chdir('chapter8')
# os.getcwd()    #이제 챕터8 경로로 떠야함
# print(os.getcwd())
# #
# # 현재 작업 디렉터리 목록 : list 반환
# os.listdir('.')        # .을 왜 찍은건지 모르겠음 아무튼 디렉터리 불러옴
# print(os.listdir('.'))
#
# # # 디렉터리 생성 : test 생성
# # os.mkdir('test')
# # os.listdir('.')  # 위와 마찬가지로 뜨는데 테스트 추가됨
# #
# # e디렉터리 이동 : test 이동시킬 것임
# os.chdir('test')
# os.getcwd() # 지금 첫번째 상황과 비슷해짐
# print(os.getcwd())
#
#
# # # 여러 디렉터리 생성 test2,3 만들 예정
# # os.makedirs('test2/test3')
# # os.listdir('.')     # test2만 만들어짐?
# #
# # 디렉터리 이동
# os.chdir('test2')
# os.listdir('.')    #이게 test3 이라는데
# print(os.listdir())
# #
# # # 디렉터리 삭제
# # os.rmdir('test3')
# # os.listdir('.')
# #
# # 상위 디렉터리 이동 : 상위 디렉터리 2개 이동
# os.chdir('../..')
# os.getcwd()
# print(os.getcwd())
# #
# #  여러개의 디렉터리 삭제
# os.removedirs('test/test2')


# 경로관련함수

import os.path

#현재 경로 확인
os.getcwd()

# 경로변경
os.chdir('../chapter8')
os.getcwd()
print(os.getcwd())

#lecture 디렉터리의 step1_try 어쩌고로 절대 경로
os.path.abspath('chapter08.lecture.step01_try_except.py')
# 아무튼 여기로 이동시킴
print(os.path.abspath('chapter08.lecture.step01_try_except.py'))
#파일 디렉터리 이름
os.path.dirname('chapter08.lecture.step01_try_except.py')
print(os.path.dirname('chapter08.lecture.step01_try_except.py'))

#workspace 디렉터리 유무 확인
os.path.exists('chapter08.lecture.step01_try_except.py')
print(os.path.exists('chapter08.lecture.step01_try_except.py'))
# 파일 유무 확인
os.path.isfile('D:\\pywork\\workspace')
print(os.path.isfile('D:\\pywork\\workspace'))

#lecture 디렉터리 유무 확인
os.path.isdir('../chapter8/lecture')
print(os.path.isdir('../chapter8/lecture'))
#
#디렉터리와 파일 분리
os.path.split('c:\\test\\test1.txt')
print(os.path.split('c:\\test\\test1.txt'))
#디렉터리와 파일 결합
os.path.join('c:\\test','test1.txt')
print(os.path.join('c:\\test','test1.txt'))

# #파일 크기
# os.path.getsize('chapter08.lecture.step01_try_except.py')


import glob
glob.glob('test*.py')
glob.glob('c:/test[0-9]')
['c:/test1','c:test9']
glob.glob('c:/test[0-9]/*.txt')
['c:/test1\\1.txt.txt','c:/test1\\test.tx.txt','c:/test9\\10.jpg.txt']
glob.glob('c:/test[0-9]/[0-9].*')
['c:/test1\\1.txt.txt']
glob.glob('c:/test1/*.txt')
['c:/test1\\1.txt.txt','c:/test1\\test.tx.txt']
glob.glob('c:/test1/?.txt')
['c:/test1\\1.txt']
glob.glob('c:/test1/*.txt', recursive=True)
['c:/test1\\1.txt','c:/test1\\test.txt']




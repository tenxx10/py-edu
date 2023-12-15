# 이미지 파일 이동 예시
import os
from glob import glob

# 1 파일 경로 image
print(os.getcwd())
img_path = '../chapter8/images/'
img_path2 = 'chapter8/images2/'

# 디렉터리 존재 유무
if os.path.exists(img_path) :
    print('해당 디렉터리가 존재함')
    # 3 image 파일 저장, 파일 이동 디렉터리 생성
    images = []
    os.mkdir(img_path2)

    # 4 images 디렉터리에서 png 검색
    for pic_path in glob(img_path + '*.png') :

        # 5 경로와 파일명 분리, 파일명 추가
        img_path = os.path.split(pic_path)
        images.append(img_path[1])

        # 6 이진파일 읽기
        rfile = open(file=pic_path, mode='rb')
        output = rfile.read()

        # 7 이진파일 쓰기 -> 챕터8 png 이동
        wfile = open(img_path2+img_path[1], mode='wb')
        wfile.write(output)
    rfile.close(); wfile.close()

else :
    print('해당디렉토리가 없음')

# print('png file = ', images)








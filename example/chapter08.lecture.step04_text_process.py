import os

#텍스트 디렉터리 경로 지정
print(os.getcwd())
txt_data = 'chapter8/txt_data'   #상대경로 지정

#2 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)
print(sub_dir)

# 각 디렉터리의 텍스트 자료 수집 함수
def textPro(sub_dir) :
    first_txt = []
    second_txt = []

    # 디렉터리 구성
    for sdir in sub_dir :
        dirname = txt_data + sdir
        file_list = os.listdir((dirname))

    # 파일 구성
        for fname in file_list :
            file_path = dirname + '/' + fname    # 파일 구성

            #3-2 파일 선택
            if os.path.isfile((file_path)) :
                try :
                    file = open(file_path, 'r')
                    if sdir == 'first' :
                        first_txt.append(file.read())
                    else :
                        second_txt.append(file.read())

                except Exception as e :
                    print('예외발생: ', e)
                finally:
                    file.close()
    return first_txt, second_txt

# 함수호출
    first_txt, second_txt = textPro(sub_dir)

    # 5 수집한 텍스트 자료 확인
    print('first_tex 길이 =', len(first_txt))
    print('second_tex 길이 =', len(second_txt_txt))

    # 6 텍스트 자료 결합
    tot_texts = first_txt + second_txt
    print('tot_texts 길이= ', len(tot_texts))

    #7 전체 텍스트 내용
    print(tot_texts)
    print(type(tot_texts))


    #1 pickle 모듈
    import pickle   #파일 저장
    # tot_texts = []
    # pfile_w = []

    # 2 file save : write binary
    pflie_w = open('../chapter8/data/tot_texts.pck', mode='wb')
    pickle.dump(tot_texts, pfile_w)

    # 3 file load : read binary
    pfile_r = open('../chapter8/data/tot_texts.pck', mode='rb')
    tot_texts_read = pickle.load(pfile_r)
    print('tot_texts 길이=', len(tot_texts_read))

    print(type(tot_texts_read))
    print(tot_texts_read)








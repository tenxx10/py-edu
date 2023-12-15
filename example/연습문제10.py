import pymysql

config = {
    'host': '127.0.0.1',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True}

try :
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    while True :   # 무한루프문 등장 ㅋ
        print('\t[ 레코드 처리 메뉴]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')
        menu = int(input('\t메뉴번호 입력: '))


        if menu == 1 :    # 조회 ( 전체 조회 , 상품명 조회)
            sel = int(input('1. 전체 조회, 2. 상품명 조회: '))    # 여기서 1,2 로 나뉨
                # 1) 전체인 경우
            if sel == 1 :
                sql = "select * from goods"
                cursor.execute(sql)
                data = cursor.fetchall()
                # 2 가져오기
            elif sel == 2 :
                name = input('상품명 입력: ')
                sql = f"select * from goods where name like '%{name}%'"
                cursor.execute(sql)
                data = cursor.fetchall()


        elif menu == 2 :    #추가
            code = int(input('코드 입력 : '))
            name = input('상품명 입력 : ')
            su = int(input('수량 입력: '))
            dan = int(input('단가 입력 :'))

            sql = "insert into goods values({code},'{name}',{su},{dan})".format
            cursor.execute(sql)
            conn.commit()

        elif menu == 3 :    # 수정
            code = int(input('수정할 코드 입력 : '))
            su = int(input('수정할 수량 입력: '))
            dan = int(input('수정할 단가 입력 :'))

            sql = f"update goods set su={su}, dan={dan}, where code={code}"
            cursor.execute(sql)
            conn.commit()

        elif menu == 4 :
            code = int(input('삭제할 코드 입력 : '))
            sql = f"delete from goods where code = {code}"
            cursor.execute(sql)
            conn.commit()


        elif menu == 5 :
            print('프로그램 종료')
            break

        else:
            print('해당 메뉴는 없습니다.')

except Exception as e :
    print('db error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

    # 문제 2

import ptmysql










''' CRUD : Create, Read, Update, Delete '''

import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    sql = """ create table if not exists goods(
                    code int primary key,
                    name varchar(30) not null,
                    su int default 0,
                    dan int default 0)"""
    cursor.execute(sql)

    code = int(input('코드 입력 : '))
    name = input('상품명 입력 : ')
    su = int(input('수량 입력: '))
    dan = int(input('단가 입력 :'))

    # sql = "insert into goods values({code},'{name}',{su},{dan})"
    sql = "insert into goods values({code},'{name}',{su},{dan})".format
    cursor.execute(sql)
    conn.commit()

    sql='select * from goods'
    cursor.execute(sql)
    rows = cursor.fetchall()

    for r in rows :
        # 프린트로 튜플 타입 뽑을 것임 r
        print('%d   %s    %d    %d'%r)

    print('검색 레코드 수:', len(rows))

    name = input('\n조회할 상품명 입력:')
    sql = f"select*from goods where name like '%{name}%' "
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        for r in rows :
            print(r[0], r[1], r[2], r[3])
    else :
        print('해당상품 없음')

except Exception as e :
    print('db 연동 오류: ', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()


# import pymysql
#
# config = {
#     'host': '127.0.0.1',
#     'user': 'scott',
#     'password': 'tiger',
#     'database': 'work',
#     'port': 3306,
#     'charset': 'utf8',
#     'use_unicode': True
# }
#
# try:
#     conn = pymysql.connect(**config)
#     cursor = conn.cursor()
#
#     # 테이블이 존재하지 않을 때만 테이블을 생성
#     cursor.execute("SHOW TABLES LIKE 'goods'")
#     if cursor.fetchone() is None:
#         sql = """CREATE TABLE goods(
#                     code INT primary key,
#                     name VARCHAR(30) NOT NULL,
#                     su INT DEFAULT 0,
#                     dan INT DEFAULT 0)"""
#         cursor.execute(sql)
#         print("테이블 'goods'가 생성되었습니다.")    #확인 문구임
#
#     code = int(input('코드 입력 : '))
#     name = input('상품명 입력 : ')
#     su = int(input('수량 입력: '))
#     dan = int(input('단가 입력 :'))
#
#     sql = "INSERT INTO goods VALUES({}, '{}', {}, {})".format(code, name, su, dan)
#     cursor.execute(sql)
#     conn.commit()
#
#
#     sql='select * from goods'
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#
#     for r in rows :
#         # 프린트로 튜플 타입 뽑을 것임 r
#         print('%d   %s    %d    %d'%r)
#
#     print('검색 레코드 수:', len(rows))
#
#     name = input('\n조회할 상품명 입력:')
#     sql = f"select*from goods where name like '%{name}%' "
#     cursor.execute(sql)
#     rows = cursor.fetchall()
#
#     if rows :
#         for r in rows :
#             print(r[0], r[1], r[2], r[3])
#     else :
#         print('해당상품 없음')
#
#
# except Exception as e:
#     print('db 연동 오류: ', e)
#     conn.rollback()
#
# finally:
#     cursor.close()
#     conn.close()

######## 2번
''' CRUD : Create, Read, Update, Delete '''

import pymysql

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    '''
    sql = """ create table goods(
                    code int primary key,
                    name varchar(30) not null,
                    su int default 0,
                    dan int default 0)"""
    cursor.execute(sql)
    '''

    # 레코드 추가
    '''
    code = int(input('코드 입력 : '))
    name = input('상품명 입력 : ')
    su = int(input('수량 입력: '))
    dan = int(input('단가 입력 :'))

    # sql = "insert into goods values({code},'{name}',{su},{dan})"
    sql = "insert into goods values({code},'{name}',{su},{dan})".format
    cursor.execute(sql)
    conn.commit()
    '''

# 레코드 수정
    ''' 
    code = int(input('수정할 코드 입력 : '))
    name = input('수정할 상품명 입력 : ')
    su = int(input('수정할 수량 입력: '))
    dan = int(input('수정할 단가 입력 :'))
    
    sql = f"update goods set name='{name}', su={su}, dan={dan}, where code={code}"
    cursor.execute(sql)
    conn.commit()
    '''

     # 레코드 삭제
    code = int(input('삭제할 코드 입력 : '))
    sql = f"select * from goods where code = {code}"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        print('레코드 삭제')

        '''
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql)
        conn.commit()
        '''
    else:
        print('해당내용 없음')

    sql='select * from goods'
    cursor.execute(sql)
    rows = cursor.fetchall()
    # print(type(dataset))     #class tuple

    for r in rows :
        # 프린트로 튜플 타입 뽑을 것임 r
        print('%d   %s    %d    %d'%r)

    print('검색 레코드 수:', len(rows))

    #상품명 조회
    name = input('\n조회할 상품명 입력:')
    sql = f"select*from goods where name like '%{name}%' "
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        for r in rows :
            print(r[0], r[1], r[2], r[3])
    else :
        print('해당 상품 없음')


except Exception as e:
    print('db 연동 오류: ', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()



















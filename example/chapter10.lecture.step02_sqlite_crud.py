import sqlite3

try :
    conn = sqlite3.connect('../chapter10/data/sqlite_db')   # 연동시켜줌
    cursor = conn.cursor()    #sql 실행객체 만들어줌

    sql = """create table if not exists goods(
    code interger primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0
    )"""
    cursor.execute(sql)

    cursor.execute("insert into goods values(1,'냉장고',2,850000)")
    cursor.execute("insert into goods values(2,'세탁기',3, 550000)")
    cursor.execute("insert into goods(code,name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 1500000)")
    conn.commit()

    # 레코드 조회
    sql = "select * from goods"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows :
        print(row[0], row[1], row[2], row[3])
        print('검색된 레코드 수 :', len(rows))

    # 상품명 조회
    name = input("상품명 입력: ")
    sql = f"select * from goods where name like '%{name}'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows :
        for row in rows :
            print(row)

    else :
        print('검색된 레코드 없음')

except Exception as e :
    print('db 연동 error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()

##################

import sqlite3

try :
    conn = sqlite3.connect('../chapter10/data/sqlite_db')   # 연동시켜줌
    cursor = conn.cursor()    #sql 실행객체 만들어줌

    sql = """create table if not exists goods(
    code interger primary key,
    name text(30) unique not null,
    su integer default 0,
    dan real default 0.0
    )"""
    cursor.execute(sql)

    cursor.execute("insert into goods values(1,'냉장고',2,8500000)")
    cursor.execute("insert into goods values(2,'세탁기',3, 550000)")
    cursor.execute("insert into goods(code,name) values(3, '전자레인지')")
    cursor.execute("insert into goods(code, name, dan) values(4, 'HDTV', 1500000)")
    conn.commit()

# 레코드 추가
    code = int(input('code 입력: '))
    name = input('name 입력: ')
    su = int(input('su 입력: '))
    dan = int(input('dan 입력:'))

    sql = f"insert into goods values({code},'{name}',{su},{dan}"
    cursor.execute(sql)
    conn.commit()

    sql = "select * from goods"
    cursor.execute(sql)
    row = cursor.fetchall()

    for row in rows:
        print(row[0], row[1], row[2], row[3])

    print('검색된 레코드 수 :', len(rows))

    name = input('상품명 입력: ')
    sql = f"select * from goods where name like '%{name}%"
    cursor.execute(sql)
    row = cursor.fetchall()

    if rows :
        for row in rows :
            print(row)

    else :
        print('검색된 레코드 없음')

except Exception as e :
    print('db 연동 error :', e)
    conn.rollback()

finally:
    cursor.close()
    conn.close()


import pymysql
print(pymysql.version_info)

# insert into goods values(1,'냉장고',2,8500000)
# insert into goods values(2,'세탁기',3, 550000)
# insert into goods values(3, '전자레인지', 2, 350000)
# insert into goods values(4, 'HDTV', 3, 1500000)

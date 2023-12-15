'''sqlite3 - 내장형 DMBS'''
# 패키지 import

import sqlite3
print(sqlite3.sqlite_version_info)    # 3,21,0

try :
    conn = sqlite3.connect('../chapter10/data/sqlite_db')
    cursor = conn.cursor()

    # table 생성
    sql = "create table if not exists test_table(name text(10), phone text(15), addr text(50))"
    cursor.execute(sql)


    cursor.execute("insert into test_table values('홍길동','010-1111-1111','서울시')")
    cursor.execute("insert into test_table values('이순신','010-2222-2222','해남시')")
    cursor.execute("insert into test_table values('강감찬','010-3333-3333','평양시')")
    conn.commit()

    cursor.execute("select * from test_table")
    rows = cursor.fetchall()

    for row in rows :
        print(row)

    print('이름 \t전화번호 \t주소')    # 레코드 출력
    for row in rows :
        print(row[0], '\t',row[1],'\t',row[2])

except Exception as e :
    print('db 연동 실패 : ', e)
    conn.rollback()

finally :
    cursor.close()
    conn.close()

















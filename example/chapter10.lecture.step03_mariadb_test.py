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

    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()

    print(tables)

    if tables:
        print('table 있음')
    else :
        print('table 없음')

except Exception as e :
    print('db error :', e)

finally:
    cursor.close()
    conn.close()



# 218.154.114.209 아이피 주소


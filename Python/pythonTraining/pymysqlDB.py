import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='password', db='데이터베이스 이름', charset='utf8')
cur = conn.cursor()
sql = "SELECT * FROM 테이블 명"
cur.execute(sql)
result = cur.fetchall()
for row in result:
    print(row)
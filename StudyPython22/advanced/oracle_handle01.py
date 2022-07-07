# 오라클 DB 연동
import cx_Oracle as ora

# 데이터 소스 네임 객체 생성(접속주소, 포트번호, 서비스명)
dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
# DB 연결 객체
conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')

cur = conn.cursor() # 커서 생성
query = 'SELECT * FROM emp'

for row in cur.execute(query):
    print(row)

cur.close() # 필수 !!
conn.close() # 필수 !!


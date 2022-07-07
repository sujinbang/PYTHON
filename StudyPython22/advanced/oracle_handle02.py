# 오라클 DB 연동
import cx_Oracle as ora

#DB 접속함수
def myconn():
    # 데이터 소스 네임 객체 생성(접속주소, 포트번호, 서비스명)
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    # DB 연결 객체
    conn = ora.connect(user = 'scott', password = 'tiger', dsn = dsn, encoding = 'utf-8')
    return conn

def test01(conn):
    cur = conn.cursor() # 커서 생성
    query = 'SELECT * FROM emp'

    for row in cur.execute(query):
        print(row)

    cur.close()
    conn.close()

def test02(conn):
    cur = conn.cursor() # 커서 생성
    query = 'SELECT * FROM emp'
    cur.execute(query)

    while True:
        row = cur.fetchone()
        if row is None: break
        print(row)

    cur.close()
    conn.close()

if __name__ == '__main__':
    print('-----SQL조회 기본 실행-----')
    test01(myconn())
    print('---- SQL 조회 fetchone 사용 ----')
    test02(myconn())


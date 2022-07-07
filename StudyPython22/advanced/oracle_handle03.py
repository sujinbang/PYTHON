# DB연동 - INSERT INTO
import cx_Oracle as ora

# DB접속
def myconn():
    dsn = ora.makedsn('localhost', 1521, service_name = 'orcl')
    conn = ora.connect(user='scott', password='tiger', dsn = dsn, encoding='utf-8')

    return conn

def get_list(conn):
    cur = conn.cursor() # 실행 결과 데이터를 담을 메모리 객체
    for row in  cur.execute("SELECT * FROM divTBL"):
        print(row)
    
    cur.close()
    conn.close()

def set_list(conn,tup):
    cur = conn.cursor()
    query = "INSERT INTO divtbl VALUES (:1, :2)" # SQL Inject 보안문제 + 사용효율성
    cur.execute(query, tup)
    conn.commit() # 완전 저장
    cur.close()
    conn.close()

if __name__ =='__main__':
    print('Divtbl 데이터 조회')
    get_list(myconn())
    print('DIVTBL 신규 입력')
    division, names = input('(division,names) 입력 (구분자 \' \') > ').split(' ')
    tup = (division, names)
    set_list(myconn(), tup)

    print('입력 후 Divtbl 데이터 조회')
    get_list(myconn())


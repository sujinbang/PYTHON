# CSV파일 읽기
#한글 인코딩 : utf-8, cp949(ANSI)
import csv

file_name = './busanbus.csv'

f = open(file_name, mode = 'r', encoding = 'utf-8')
reader = csv.reader(f, delimiter=',') # 구분자가 ,일 경우
next(reader) # header 삭제


for line in reader:
    print(line)

f.close() ## 필수!!
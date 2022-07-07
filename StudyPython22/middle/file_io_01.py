# 파일 입출력 1 - 쓰기

# mode = w 새로생성쓰기 a 추가쓰기 r 읽기

f = open(file = 'C:/STUDY/StudyPython22/temp.txt', mode='w', encoding = 'utf-8')

f.write('안녕하세요.\n')
f.write('저는 방수진입니다.\n')
f.write('한국사람입니다.\n')

f.close() ## 필수
print('파일 생성 완료')
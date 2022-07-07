# 문자열 처리함수
#   - lower(), upper(), isupper(), len()
#   - replace(), index(), find(), count()

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)   # 두번째 n 출력

print(python.find("Java"))   # 원하는 값이 없을 때 : -1 반환
#print(python.index("Java"))  # 오류발생 - 프로그램 종료

print(python.count("n"))


# 문자열 포맷
# print("a" + "b")
# print("a", "b")


# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요" % "파이썬")
print("Apple 은 %c로 시작해요." %"A")
# %s
print("나는 %s색과 %s색을 좋아해요" % ("파란", " 빨간"))


# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {0}색과 {1}색을 좋아해요".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))


# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요".format(color="빨간", age = 20))

# 방법 4 (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")


# 탈출문자
# \n : 줄바꿈
#\" \' : 문장 내에서 따옴표

print("백문이 불여일견\n백견이 불여일타")

# 저는 "나도코딩"입니다.
print("저는 '나도코딩' 입니다")
print('저는 "나도코딩" 입니다')
print("저는 \"나도코딩\" 입니다")

# \\ : 문장 내에서 \
print("C:\\STUDY\\StudyPython2")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
print("Yellow Apple\rPine")

#\b : 백스페이스(한글자 삭제)
print("Redd\bApple")

#\t : 탭
print("Red\tApple")


#--------------------------------------
# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
#   예) 생성된 비밀번호 : nav51!

# 내 답안
user = input("사이트 주소를 입력하세요:")
string = user
string = string[7:]
string = string.split('.')[0]

print(string[:3] + str(len(string)) + str(string.count("e")) + '!')


# 답안
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2
#my_str[0:5] -> 0 ~ 5 직전까지. (0,1,2,3,4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1}입니다".format(url, password))






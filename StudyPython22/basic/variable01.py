# 주석입니다. 주석은 프로그래밍에 영향을 끼치지 않습니다.

# 변수
a = '안녕하세요' # "안녕하세요", "I'm a boy."
print(a)

a = True
print(a)

a = 3.14
print(a)

a = 1/10
print(a)

print('값은', a, '입니다') #출력 방식 2 ,로 구분 갯수는 상관 X


a = 3 # 정수형
b = 3.141592 # 실수형
c = 'python' # 문자열형
d = (1, 2, 3) # 튜플 - 삭제, 변경 불가능
e = [4, 5, 6] # 리스트 - 삭제, 변경 가능
f = [7, '8', True] 
g = False # T : 1 / F : 0 (문자열 X)
print('변수의 값', 'a=', a, 'b=', b, 'c=', c, 'd=', d)
print('변수의 값', 'e=', e, 'f=', f, 'g=', g)

# 변수명은 숫자로 시작할 수 없다
# '_'만 변수명에 넣을 수 있는 특수문자이다
# var6 != Var6

Var5 = 5
var5 = '8'
print(Var5, var5)

print(id(a)) # 각 변수의 주소
print(id(b))
print(id(c))
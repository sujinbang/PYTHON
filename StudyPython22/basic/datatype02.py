#문자열
bruce_eckel = 'Life is short.\n\tYou need Python.'
print(bruce_eckel)

#탈출문자 : \n. \t

#여러줄 문자열
multi_line = '''Life is short.
You need Python.
And I need C#, too.
'''

print(multi_line)

#리스트(배열)
b = [1,2,3,4]

print(b)

#프로그래밍에서 배열의 시작은 0부터

b.append(5) #리스트 맨 마지막 추가
print(b)

b.insert(3,10) #원하는 인덱스에 추가
print(b)

b.sort() # ascending(오름차순)
print(b)

b.reverse() # descending(내림차순)
print(b)

b.remove(10) # 원소 삭제
print(b)

print(type(b))
print(b[2])

# 튜플
c = (1,2,3,4)
print(c)
# c.append(5) -- 튜플은 값을 추가,수정,삭제할 수 없음
print(c[2])


#딕셔너리 key : value 쌍의 집합
spiderman = {
    'name' : '피터 파커',
    'age' : 18,
    'weapon' : '웹슈터',
    'memberOfAvengers' : True
}

print(spiderman)
print(spiderman['name'])
print(spiderman['memberOfAvengers'])




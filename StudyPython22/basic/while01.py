# while 문 학습
hit = 0

while (hit <100) :
    hit += 1

    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10:
        print('나무가 넘어갑니다!!')
        break
    else:
        print('아직 안넘어감')

print('나무찍기완료')


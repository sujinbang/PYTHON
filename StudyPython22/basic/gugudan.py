# 구구단 프로그램
# 2x1 = 2 ... 2x9 = 18
# 3x1 ... 3x9
#........9x9

print('----구구단 프로그램----')

for x in range(2,10) :
    print(f'{x}단 시작')
    for y in range(1,10):
        print(f'{x}*{y}={x*y:2d}', end=' ')
    print() #단마다 줄맞추기




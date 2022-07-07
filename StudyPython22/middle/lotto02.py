# 번호 가중치를 준 로또 프로그램
import random as rnd

numbers = weights = list(range(1,46))
lotto = []
rnd.shuffle(weights)


lotto = rnd.choices(numbers, weights = weights, k=6)
lotto.sort()
print(lotto)

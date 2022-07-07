# for
# starbucks = ['아이언맨', '토르', '아이엠 그루트']
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))

# # 출석번호가 1 2 3 4, 앞에 100을 붙이기로함 -> 101 102 103 104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)

#-----------------------------------------------------------------------

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는
# 프로그램을 작성하시오.

# 조건 1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분


import random
i = 0
for customer in range (1, 51):
    min = random.randrange(5,51)   
    if (min >= 5) & (min <= 15):
        print("[0] {}번째 손님 (소요시간 : {}분)".format(customer, min))
        i += 1
    else :
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(customer, min))

print("총 탑승 승객 : {}분".format(i))

# 답안
# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1, 51) : #1 ~ 50 이라는 수(승객)
#     time = randrange(5, 51) # 5 ~ 50분 소요 시간, 탑승 승객 수 증가 처리
#     if 5 <= time <= 15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else :
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
# print("총 탑승 승객 : {}분".format(cnt))
for i in range(5):
    print(i)
print()
for i in reversed(range(5)):
    print(i)

# 구구단
# 구구단인데 3단씩 옆으로


for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print(f"{i} x {j} = {i*j}")
print("-" * 30)
# for i in range(2, 10, 3):
#     for j in range(1, 10, 1):
#         if i + 2 < 10:
#             print(
#                 f"{i} x {j} = {i*j} \t {i+1} x {j} = {(i+1)*j} \t {i+2} x {j} = {(i+2)*j}"
#             )
#         else:
#             print(f"{i} x {j} = {i*j} \t {i+1} x {j} = {(i+1)*j}")


# 2 3 4
# 2 * 1 = 2 3 * 1 = 3 4 * 1 = 4
# 2 * 2 = 4 3 * 2 = 6 4 * 2 = 8
# 2 * 3 = 6 3 * 3 = 9 4 * 3 = 12
# 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16
# 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20
# 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24
# 5 6 7
# 8 9

# for i in range(10):
#     if i > 0:
#         if i % 3 == 0:
#             print(f"2 x {i} = {2*i}")
#         else:
#             print(f"2 x {i} = {2*i}", end=" ")

# for i in range(10):
#     if i > 0:
#         if i % 3 == 0:
#             print(f"3 x {i} = {3*i}")
#         else:
#             print(f"3 x {i} = {3*i}", end=" ")

import random

print(random.random())
print(random.randint(1, 6))

# 주사위 3이 몇 번만에 나오는지 출력하시오

cnt = 1
# dice = [1, 2, 3, 4, 5, 6]
# while (random.choice(dice) == 3):
#     if not (random.choice(dice) == 3):
#         cnt += 1
# print(f"주사위 3이 나오기까지 {cnt}회 걸렸습니다.")

while random.randint(1, 6) != 3:
    cnt += 1
print(f"주사위 3이 나오기까지 {cnt}회 걸렸습니다.")

"""
            ____+____
            ___+++___
            __+++++__
            _+++++++_
            +++++++++
"""

# 줄마다 + 2n-1
# 혹은 2n + 1
# ' '는 range(4 = (반복 끝 - 1))로 양쪽

# endLine = 5
# start = 0
start = int(input("몇 번째 줄에서 시작할지 입력하세요."))
endLine = int(input("출력할 줄 수를 입력하세요."))
for i in range(start, endLine):
    # print(i)
    print(" " * (endLine - i - 1), end="")
    print("*" * (2 * i + 1), end="")
    print()

import turtle as t

t.shape("turtle")

# while True:
#     print(1)
# 무한루프 돌 때 ctrl+c 누르면 KeyboardInterrupt 에러 뜨면서 중단됨

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
    else:
        print(i)

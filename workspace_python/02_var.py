a = 10
print(a)

b = 5 / 2
print(b)

# b = 5 / 0 # ZeroDivisionError: division by zero
# print(b)

c = 5 // 2
print(c)

d = -5 // 2  # 내림. -2가 나올 거라 생각할 수 있으나 내림이라 -3
print(d)

e = 4**2  # 제곱
print(e)

# e++ # 없음
# e-- # 없음
e = e + 1
e **= 2
print(e)

print(int(2.4))
print(int(-2.4))  # 소수점 버림
print(int("10") + 1)
# print(int('a'))

print(0.123445555678921345678901234567890)

print(type(10))
print(type("10"))

print(4.3 - 2.7 == 1.6)  # False

print(4.2 + 5)

print(float(5))
print(float("5.2"))

a = 10
b = "오백원"

# 전통적인 swap
"""
c = a
a = b
b = c
"""

a, b = b, a
print(a)  # 오백원
print(b)  # 10

a = input("입력하세요:")
print(a)

a = input("첫 번째 숫자를 입력하세요: ")
b = input("두 번째 숫자를 입력하세요: ")

print(int(a) + int(b))

print(1, 2)
print(1, 2, sep=" ")
print(1, 2, sep=",")

print(1, end="")
print(2)

print(1 == 1.0)
print(1 is 1.0)  # === 즉, 타입까지 같다.
print(1 is not 1.0)  # !==

print(1, False or False and not False)

a = False
b = a or "쉬는시간"
print(b)

print(3 < 5 < 7)

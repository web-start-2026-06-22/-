a = []
b = list()
print(type(a))
print(type(b))

a = [1, 2, 3]
print(a)

# range
# 전달인자 1개 : 0 ~ 바로 숫자 앞 까지
c = range(10)
print(c)
print(list(c))  # nodeList 같은 유사배열 느낌

# 전달인자 2개 : 첫 번째 부터 두 번째 바로 앞
d = range(5, 12)
print(list(d))

e = range(12, 5)  # []
print(list(e))

# 전달인자 3개 : 첫 번째 부터, 두 번째 바로 앞 까지, 세 번째씩 건너 뛰기
f = range(-4, 10, 2)
print(list(f))

a = [0, 1, 2, 3, 4, 5]
a = list(range(6))

del a[3]

print(a)

a = a + [6]
print(a)

a += [7]
print(a)

a.append(8)
print(a)

b = [9, 10]
a.append(b)
print(a)

print(":=" * 3)
c = [654, 156, 964, 15, 35]
c.sort()
print(c)
c.sort(reverse=True)
print(c)

c = c[::-1]
print(c)

c.reverse()
print(c)

d = c.pop()
print(c, d)

c.insert(0, 100)
print(c)

c.insert(10, 200)  # index를 벗어나면 걍 끝에
print(c)

c.extend([1, 2])  # 리스트를 합쳐준다.
print(c)

a = [1, 2, 3, 4, 2]
a.remove(2)  # 처음 만나는 값을 찾아서 지운다.
print(a)

if 5 in a:
    a.remove(5)  # 없는 값은 에러난다.

a = [1, 2, 3, 4, 2, 4]
b = a.index(2)
print(b)
# b = a.index(5)  # 없는 값은 에러
# print(b)

c = a.count(4)
print(c)

a.reverse()
print(a)
# b = reversed(a)
# print(b)

a.clear()
print(a)
a = []

a = [1, 2, 3]
print(a[len(a) :])
# print(a[3])
print(a[3:])

# a[3:] = 4 #TypeError: must assign iterable to extended slice
a[3:] = [4, 5, 6]
print(a)

a = [1, 2, 3, 4, 5]
b = a
b[2] = 30
print(b)
print(a)

a = [1, 2, 3, 4, 5]
b = a.copy()
b[2] = 30
print(b)
print(a)

a = [10, 20, 30]
for i in a:
    print(i)

# 이번 턴의 index, value를 한번에 뽑아 줌.
for index, value in enumerate(a):
    print(index, value)

# 시작 인덱스 지정 가능
for index, value in enumerate(a, start=100):
    print(index, value)

print("-" * 30)
a = [7, 3, 5, 8, 4]
b = a[0]
for i in range(len(a)):
    if b < a[i]:
        b = a[i]
    else:
        pass
print(f"가장 큰 수는 {b}입니다.")
print("-" * 30, "a 초기화")
a = []
# a 배열에 0~9까지 넣기
for i in range(10):
    a.append(i)
print(a)

a = [i for i in range(10)]
a = [i * 2 for i in range(10)]

a = []
for i in range(10):
    if i % 2 == 0:
        a.append(i)

a = list(i for i in range(10) if i % 2 == 0)
print(a)

a = [1.2, 2.5, 3.7, 4.6, -3.5]
# for i in range(len(a)):
#     a[i] = int(a[i])
for i, value in enumerate(a):
    a[i] = int(value)
print(a)

# 두 번째 반복되는 것을 하나씩 꺼내서
# 첫 번째 함수에 넣고
# 결과를 배열같은 순차적 자료형으로 만들어 준다.
a = list(map(int, a))
# a = map(int, a) #<map object at 0x0000016EF7152C80> at 뒤가 주소.
print(a)

a = [[10, 20], [30, 40], [50, 60]]
print(len(a))
print(a[1][0])

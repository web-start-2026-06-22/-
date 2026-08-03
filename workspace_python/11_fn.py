# hello() # 인터프리터, 위에서부터 한 줄 한 줄 읽기 때문에 에러
# js는 호이스팅이 일어나기 때문에 가능.


def hello():
    print("hello world")


hello()


def add(a, b):
    # __doc__
    # 함수 첫줄의 따옴표로 감싸진 주석 글씨를 출력해준다.
    "a + b를 출력"
    print(a + b)


add(1, 2)
print(add.__doc__)


def add2(a, b):
    return a + b


c = add2(1, 2)
print("add2 실행 결과:", c)


def 아낌없이주는함수():
    return 100


d = 아낌없이주는함수()
print(d)


def not_ten(a):
    if a == 10:
        return  # return 값 안 줬을 때 None
    print(a, "입니다.", sep="")


b = not_ten(10)
print("b:", b)


def add_sub(a, b):
    x = a + b
    y = a - b
    # return (x, y) # 튜플이라서 튜플 한 덩어리를 리턴해주는 것
    return x, y


c = add_sub(1, 2)
print(type(c), c)

d, e = add_sub(1, 2)

a = add_sub(1, 2)
print(a)

# x = add_sub(1, 2, 3)
# TypeError: add_sub() takes 2 positional arguments but 3 were given
# js와 다르게 함수의 전달 인자 개수와 맞춰줘야 함.


def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)


a = [1, 2, 3]
print(a)
print(*a)  # print(1,2,3)과 같은 형태
# print_numbers(a)
print_numbers(*a)


def print_numbers2(*a):
    print(type(a), a)
    for b in a:
        print(b)


print_numbers2(1)
print_numbers2(1, 2, 3, 4)


def print_numbers3(c, *a):
    print(c)
    for b in a:
        print(b)


# def print_numbers3(*a, c) : # 어디부터 어디까지 가변 인수 *a인지 모르니까


def minus(x, y):
    print(x - y)


minus(5, 2)
minus(y=5, x=2)

x = {"name": "아무개", "age": 28}


def info(age, name):
    print(age, name)


info(*x)  # 딕셔너리의 경우 *는 key만 추출
info(**x)  # key=value, key=value 형태로 바뀌게 된다.
# dict(name="김이박최더보기아무개", age=24)


def info2(**a):
    for k, v in a.items():
        print(k, v)


info2(**x)


def info3(name, age, addr="비공개"):
    print(name, age, addr)


info3(1, 2, 3)
info3(1, 2)

"""

def 파일출력(경로) :
    경로 안의 모든 목록 뽑아오기
    if not folder :
        print(경로, 파일명)
    elif folder : 
        파일출력(folder)
        
"""


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def local_var():
    a2 = 10
    print(a2)


local_var()
# print(a2) # a2는 local_var의 지역 변수라서 현 시점엔 없다.


def ref(a):
    a.append(4)


b = [1, 2, 3]
ref(b)
print(b)


def fn1(a):
    return a + 10


def fn2(a):
    return a * 10


c = 10
b = fn1(c)  # 20
print(b)
d = fn2(b)  # 200
print(d)

e = fn2(fn1(c))
print(e)

print(fn1)
# print = 2


def ten(x):
    return x + 10


ten2 = lambda x: x + 10
print(ten2(5))
print((lambda x: x + 10)(5))

a = ["1", "2"]
b = [int(a[0]), int(a[1])]
c = list(map(int, a))
print(a, b, c)

d = list(map(ten2, c))
print(d)

e = list(map(lambda x: x + 10, c))
print(e)


def square(x):
    # return x * x
    return x**2


sqr = lambda x: x**2
print(sqr(2))


def sum(x, y):
    return x + y


add = lambda x, y: x + y
print(add(3, 5))

info = [
    {"name": "이름1", "age": 25},
    {"name": "이름2", "age": 23},
    {"name": "이름3", "age": 30},
]
# 함수로
# 나이만 출력
# lambda로도 만들어보자


def print_age(info):
    a3 = []
    for i in info:
        a3.append(i["age"])
    return a3


print(print_age(info))

print_age2 = lambda info: [p["age"] for p in info]
print(print_age2(info))


def age(info):
    return info["age"]


info.sort(key=age)
info.sort(key=lambda x: x["age"])
print(info)

x = 10  # 전역 변수 global 변수 global variable


def foo():
    x = 20  # 지역 변수.
    print("foo 안에서 x", x)


foo()
print("foo 밖에서 x", x)


def foo2():
    print("foo2 안에서 x", x)  # 전역 변수 읽기는 됨.


foo2()


def foo3():
    global x  # global은 중요
    x = 20


foo3()
print("foo3 이후에 x:", x)

# 함수 안에서 변수 우선 순위
"""
    1. 먼저 지역 변수 찾기
    2. 없으면 전역 변수 찾기
    3. 없으면 에러

"""

x = 10


def test(z):
    return z + 2


x = test(x)
print(x)


def test2(z):
    global x
    x = x + 2


print(x)

x = 10
y = 20


def test3():
    global x, y
    x = 11
    y = 12


def A():
    x = 10
    y = 20

    def B():
        x = 30

        def C():
            nonlocal x, y
            print(x)
            print(y)

        C()

    B()


A()


# def Fibonacci(n):
#     if n == 0:
#         return 0

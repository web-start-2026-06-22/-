class Person:
    # __init__
    # 클래스가 생성될 때
    # 자동으로 먼저 실행되는 메소드
    def __init__(self):
        print(1)
        self.hello = "안녕하세요"

    def greeting(self):
        # def greeting(): # self 안 넣으면 error
        # TypeError: Person.greeting() takes 0 positional arguments but 1 was given
        print(self.hello)

    def hello(self):
        self.greeting()


print(0)
james = Person()
print(2)
james.greeting()

print(james)
print(type(james))


class Person2:
    def __init__(self, name, age):
        print("__init__ 실행")
        self.hello = "안녕하세요"
        self.name = name
        self.age = age

    def greeting(self):
        print(f"{self.hello}! 저는 {self.name}이고 나이는 {self.age}입니다")


a = Person2("아무개", 20)
a.greeting()
print(a.hello)
print(a.name)

b = Person2("김이박최더보기아무개", 25)
b.greeting()
print(b.name)

b.addr = "천안"
print(b.addr)

# print(a.addr)
b.__init__(1, 2)


class Person3:
    def __init__(self, money):
        self.hello = "안녕하세요"
        self.__money = money
        # self.___money = money

    def pay(self, price):
        self.__money -= price
        print("남은 돈 : ", self.__money)
        self.__study()

    def __study(self):
        print("히히 나 혼자 레벨 업")


a = Person3(10000)
a.pay(3000)
# print(a.__money)
a.__money = 99999999999  # 이건 변수 추가
a.pay(3000)
# a.__study()

# __ 붙은 변수나 함수는
# 내부에서는 접근 가능하고
# 외부로 노출되지 않는다
# 캡슐화, 은닉화

# print(a.___money) # __ + _money


class Knotted:

    brand = "노티드-디저트맛집"

    def __init__(self, name, addr):
        # self.brand = "노티드-디저트맛집"
        self.name = name
        self.addr = addr


k1 = Knotted("천안점", "천안")
k2 = Knotted("아산점", "아산")

print(k1.name, k1.brand)
print(k2.name, k2.brand)

print(k1.name, Knotted.brand)
print(k2.name, Knotted.brand)


class Calc:
    PI = 3.141592

    def __init__(self):
        self.meet = 200

    # def plus(self, x, y):
    #     return Calc.add(x, y)

    @staticmethod
    def add(x, y):
        return x + y

    def plus(self, x, y):
        return Calc.add(x, y)


print(Calc.add(1, 2) * Calc.PI)

a = Calc()
print(a.plus(1, 2))


class Person4:
    count = 0

    def __init__(self):
        Person4.count += 1

    @classmethod
    def print_count(cls):
        print(f"{cls.count}명 생성 됨")


p1 = Person4()
p2 = Person4()
p3 = Person4()
Person4.print_count()

"""
문제1
멜론 차트 관리 시스템
모든 곡을 리스트로 관리
한 곡에 해당하는 클래스부터 만들자
- 제목, 가수명, 앨범명, 가사

두 곡 이상 정보를 저장
각 곡의 '제목-가수명'을 출력

문제2
휴먼잡스 계정 관리 시스템
내 계정에는 id, pw, 주소가 있다
모두 접근 제한된 private 변수입니다.

메소드를 이용해서 주소를 변경하거나
주소를 return하는 메소드를 만들기

문제3
디저트 카페 노티드 창업을 위한 클래스
 - 상호, 자본금이 필수 요소

노티드를 두군데에 창업할 것이다.
하나를 창업할 때 필수 요소를 꼭 넣어야 생성되도록 만드세요


"""

print("Q1")


class Q1_melonSong:
    count = 0

    def __init__(self, title, singer, album, lyric):
        Q1_melonSong.count += 1
        self.title = title
        self.singer = singer
        self.album = album
        self.lyric = lyric


song1 = Q1_melonSong(
    "만찬가",
    "태연(TAEYEON)",
    "J-POP REMAKE Vol.1",
    "난 수십 번의 긴 밤을 보낸다 해도 얻지 못할 듯한",
)


song2 = Q1_melonSong(
    "너의 모든 순간",
    "성시경",
    "별에서 온 그대 OST Part.7",
    "너의 모든 순간 그게 나였으면 좋겠다",
)
song3 = Q1_melonSong("너에게 닿기를", "10cm", "너에게 닿기를", "이어져 가서는 닿기를")
q1List = [song1, song2, song3]
# print(len(q1List))
for i in q1List:
    print(f"{i.title}-{i.singer}")

print("-" * 30)

print("Q2")


class Q2_humanJobs:
    count = 0

    def __init__(self):
        Q2_humanJobs.count += 1
        self.__id = ""
        self.__pw = ""
        self.__addr = ""

    def changeAddr(self, addr):
        self.__addr = addr

    def displayAddr(self):
        return self.__addr


member1 = Q2_humanJobs()
member2 = Q2_humanJobs()

# print(member1.displayAddr())
# print(member2.displayAddr())
member1.changeAddr("거제")
print(member1.displayAddr())
member2.changeAddr("서울")
print(member2.displayAddr())

print("-" * 30)

print("Q3")


class Q3_knotted:
    count = 0

    def __init__(self, logo, capital):
        Q3_knotted.count += 1
        self.logo = logo
        self.capital = capital


# knotted1 = Q3_knotted()
# TypeError: Q3_knotted.__init__() missing 2 required positional arguments: 'logo' and 'capital'
# knotted2 = Q3_knotted()
# 필수값인 전달 인자 미입력 에러.
knotted1 = Q3_knotted("노티드-천안", "2억")
knotted2 = Q3_knotted("노티드-서울", "4억")

print(knotted1.capital)
print(knotted2.capital)


class Melon:
    def __init__(self):
        self.songList = []

    def appendSong(self, song):
        self.songList.append(song)


m = Melon()
m.appendSong(song1)
m.appendSong(song2)
m.appendSong(song3)

# 딕셔너리 선언
a = {}
a = dict()
print(type(a))

b = {
    "이름": "르노어",
    "포지션": "스킬 증폭 딜러",
    "스킬": {"공격": "스타카토", "방어": "피네", "javascript": "중"},
}

print(b)

c = dict(a=10, b=20)
print(c)

# b.이름
print(b["이름"])
# print( b['이름2'])

print(b.get("이름"))
print(b.get("이름2"))  # 없으면 None
print(b.get("이름2", "이름없음"))  # 없으면 두 번째 값으로 대체

print(b["스킬"]["공격"])

print(b.get("스킬").get("공격"))

print(b.get("스킬2", {}).get("공격", 0))

b["스킬"]["궁극기"] = "고뇌의 광시곡"  # 없으면 key 만들어 줌
print(b)

print("스킬" in b)
print("공격" in b)
print("공격" in b["스킬"])
print("공격" not in b["스킬"])

print(len(b))  # key의 개수

print(len(b["스킬"]))

e = b.keys()
print(e)

f = b["스킬"].keys()
print(f)

g = b.values()
print(g)
print(list(g)[0])

h = b["스킬"].values()
print(h)

i = b.items()
print(i)

a = "hello"
print(list(a))
print(set(a))  # {'h', 'e', 'o', 'l'}
# set
#   중복을 제거해서 관리한다.
#   순서는 보장하지 않는다.

b = {
    "이름": "르노어",
    "포지션": "스킬 증폭 딜러",
    "스킬": {"공격": "스타카토", "방어": "피네", "javascript": "중"},
}

b.update(이름="르노어 랭", 포지션="스증원딜")
b.update(이름="르노어 랭", 포지션="스증원딜", 나이="26")
print(b)

c = b.pop("나이")
print(b)
print(c)
# c = b.pop("나이") #KeyError: '나이'
c = b.pop("나이", 0)  # 없으면 두 번째 값을 사용
print(c)
# c = b.pop() # 전달인자 필수
c = b.popitem()
print(c)
print(b)

a = ["a", "b", "c"]
b = {"a": 0, "b": 0, "c": 0}

c = dict.fromkeys(a)
print(c)

# key만 나온다
for i in c:
    print(i)
    print(c[i])

for k, v in c.items():
    print(k, v)
"""
문제1
numbers = [3, 7, 10, 15, 22, 8, 13]
문제1-1 : 짝수만 따로 리스트로 만들어서 출력
문제1-2 : 홀수의 합

문제 2
cart = {
    '사과': {
        '가격': 1000,
        '개수': 3
    },
    '바나나': {
        '가격': 2000,
        '개수': 4
    },
    '복숭아': {
        '가격': 1500,
        '개수': 2
    },
    '키위': {
        '가격': 2200,
        '개수': 5
    }
}
다 샀을 때 가격은?

문제3
UP/DOWN 게임 만들기
단, 맞추면 몇번째에 맞췄는지도 출력

문제4
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
이런 경우 
id/pw를 입력 받거나 변수에 넣어두고
id/pw가 맞는지 틀리는지 판단해서
"아이디가 틀립니다", "비번이 틀립니다", "로그인 성공"


문제5
랜덤 투표 시스템
한번에 a, b, c 대상에 랜덤으로 투표
문제5-1 : 100번의 투표 결과를 출력하시오
문제5-2 : 그 중 가장 득표 많은 사람의 이름과 득표 수 출력
"""

"""
문제1
numbers = [3, 7, 10, 15, 22, 8, 13]
문제1-1 : 짝수만 따로 리스트로 만들어서 출력
문제1-2 : 홀수의 합
"""
numbers = [3, 7, 10, 15, 22, 8, 13]
even_num = []
odd_num = []
odd_sum = 0
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_num.append(numbers[i])
    else:
        odd_num.append(numbers[i])
        odd_sum += numbers[i]
print(even_num)
print(odd_sum)

print("-" * 30)

"""
문제2
"""

cart = {
    "사과": {"가격": 1000, "개수": 3},
    "바나나": {"가격": 2000, "개수": 4},
    "복숭아": {"가격": 1500, "개수": 2},
    "키위": {"가격": 2200, "개수": 5},
}

# print(len(cart))  # cart 배열 길이 체크

fruit = dict.fromkeys(cart)
# print(fruit)  # cart의 key들
# print(type(fruit))

fruit_info = dict.values(cart)
# print(fruit_info)  # cart의 value

total = 0

for i in fruit_info:
    # print(i)
    # print(fruit_info[i]["가격"]) # i 자체가 fruit_info[i]를 가지고 있기 때문에 에러
    # print(i["가격"])  # 가격 잘 가져와지는지 확인
    # print(i["개수"])  # 개수 잘 가져와지는지 확인
    total += i["가격"] * i["개수"]
print(f"총액은 {total}원입니다.")

"""
문제3
UP/DOWN 게임 만들기
단, 맞추면 몇번째에 맞췄는지도 출력
"""
import random

q3_upDown = random.randint(1, 99)
# print(q3_upDown)  # 출력 확인용
q3_answer = 0
cnt = 1
# while q3_upDown != q3_answer:
#     q3_answer = int(input("1~99까지의 숫자를 입력하세요."))
#     if q3_answer < q3_upDown:
#         print(f"{q3_answer}은 맞춰야할 수보다 작습니다.")
#     else:
#         print(f"{q3_answer}은 맞춰야할 수보다 큽니다.")
#     cnt += 1
# print(f"정답입니다! 정답까지 {cnt}회 걸리셨습니다.")

"""
문제4
users = {
    "admin": "1234",
    "guest": "guest",
    "user1": "abcd"
}
이런 경우 
id/pw를 입력 받거나 변수에 넣어두고
id/pw가 맞는지 틀리는지 판단해서
"아이디가 틀립니다", "비번이 틀립니다", "로그인 성공"
"""

users = {"admin": "1234", "guest": "guest", "user1": "abcd"}

# print(len(users))

id = dict.keys(users)  # 아이디
# print(id)
# print(type(id))  # type 체크
# for i in id:
#     print(i)

pw = dict.values(users)  # 비번
# print(dict.values(users))
# print(type(pw))  # type 체크
# for i in pw:
#     print(i)

login = input("아이디와 비밀번호를 입력하세요. 띄어쓰기로 id, pw를 구분합니다.").split()
# print(login)

idError = True
pwError = True

# pwStr = " ".join(pw)
# print(pwStr)


if login == []:
    print("아이디가 입력되지 않았습니다.")
elif login != []:
    for i, idpw in enumerate(users.items()):
        if login[0] != idpw[0]:
            # print("유효하지 않은 아이디입니다.")
            pass
        elif login[0] == idpw[0]:
            idError = False
            if login[1] == idpw[1]:
                pwError = False
                # print("로그인 성공")
            else:
                pwError = True
                # print("비밀번호가 틀립니다.")
if (idError == False) and (pwError == False):
    print("로그인 성공")
elif (idError == False) and (pwError == True):
    print("비번이 틀립니다.")
elif idError == True:
    print("유효하지 않은 아이디입니다.")

# idStr = " ".join(id)
# print(idStr)

# if login == []:
#     print("아이디가 입력되지 않았습니다.")
# elif idStr.find(login[0]) == -1:
#     print("아이디가 틀립니다.")
#     if login[0] == "admin": # 0
#         if login[1] != "1234":
#             print("비번이 틀렸습니다.")
#     elif login[0] == "guest": # 1
#         if login[1] != "guest":
#             print("비번이 틀렸습니다.")
#     elif login[0] == "user1": # 2
#         if login[1] != "abcd":
#             print("비번이 틀렸습니다.")
#     # if pwStr.find(login[1]) == -1:
#     #     print("비번이 틀립니다.")
#     elif login[1] == None:
#         print("비번이 입력되지 않았습니다.")
# else:
#     print("로그인 성공")
# if login == []:
#     print("아이디가 입력되지 않았습니다.")
# else:
#     print("로그인 성공")
# print("로그인 성공") # if 문 밖에 있으면 안 되는 것

'''
문제5
랜덤 투표 시스템
한번에 a, b, c 대상에 랜덤으로 투표
문제5-1 : 100번의 투표 결과를 출력하시오
문제5-2 : 그 중 가장 득표 많은 사람의 이름과 득표 수 출력
"""
'''
import random

q5 = {"a": 0, "b": 0, "c": 0}


num = 100
vote = 0
for i in range(num):
    vote = random.randint(1, 3)
    if vote == 1:
        q5["a"] += 1
    elif vote == 2:
        q5["b"] += 1
    else:
        q5["c"] += 1
print(q5)

# first = random.randint(1, 100)
# second = random.randint(1, (100 - first))
# third = 100 - (first + second)  # random 뽑을 필요가 없다. 셋 합 100이 채워져야되니까.

# print(first, second, third)  # 의도대로 작동하는지부터 체크

# q5["a"] = first
# q5["b"] = second
# q5["c"] = third

# print(q5)

# print(type(q5))

# result = dict.values(q5)
result = -1
# elected = dict.fromkeys(q5)
elected = "a"
# print(elected)
for i, vote in enumerate(q5.items()):
    # print(vote)
    # print(type(vote))
    # print(vote[0])
    # print(vote[1])
    ### 여기까지 값 체크용
    if result < vote[1]:
        result = vote[1]
        elected = vote[0]
print(f"가장 많은 득표자는 {elected}, 득표수는 {result}입니다.")
# print(result)
# for i in result:
#     print(i)  # 값 체크
#     # if elected < result[i]:
#     #     eleceted = result[i]
#     if elected < i:
#         eleceted = i
# print(f"가장 많은 득표수는 {max(result)}입니다.")

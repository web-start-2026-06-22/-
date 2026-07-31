# w : 수정 가능
file = open("느엥.txt", "w")
file.write("eng\n123\n느엥")
file.flush()  # 버퍼가 꽉 차지 않아도 내보내기
# 즉시 반영
file.close()

# 한글 캐릭터셋
# utf-8, urc-kr, cp949
file = open("느엥2.txt", "w", encoding="utf-8")
file.write("eng\n123\n느엥")
file.close()

# r : 읽기 전용
file = open("느엥.txt", "r")
s = file.read()
file.close()
print(s)

file = open("느엥2.txt", "r", encoding="utf-8")
s = file.read()
file.close()
print(s)

print("-" * 20)
file = open("느엥.txt", "r")
# s = file.read(6)
s = file.read(10)
file.close()
print(s)

print("-" * 20)
file = open("느엥.txt", "r", buffering=1)
s = file.read()
file.close()
print(s)

text = ""
file = open("느엥.txt", "r")
while True:
    chunk = file.read(2)
    if not chunk:
        break
    text += chunk
    print(chunk)
file.close()
print(text)

file = open("예나쨩.webp", "rb")
s = file.read()
file.close()
print(s)

with open("느엥.txt", "r") as file:
    s = file.read()
    print(s)

a = [1, 2, 3, 4]
with open("array1.txt", "w") as file:
    file.write(str(a))
print(str(a))

with open("array1.txt", "r") as file:
    b = file.read()
    print(type(b), b)
    c = list(b)
    print(type(c), c)

import pickle

name = "eng"
age = 20
address = "한글"
arr = [1, 2, 3, 4]
score = {"k": 1, "k2": "val"}

with open("pickle.p", "wb") as f:
    pickle.dump(name, f)
    pickle.dump(age, f)
    pickle.dump(address, f)
    pickle.dump(arr, f)
    pickle.dump(score, f)

with open("pickle.p", "rb") as f:
    # dump 순서대로 꺼낸다
    p1 = pickle.load(f)
    print(p1)
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))
    p2 = pickle.load(f)
    print(p2, type(p2))

    print(p2["k"])
# dump한 만큼만 꺼낼 수 있다.
# p2 = pickle.load(f)
# print(p2, type(p2))

# pickle 보다 대용량에 특화된 라이브러리
# import joblib

with open("느엥.txt", "a") as f:
    f.write("123")
    # f.read()

# +
# 쓰기 계열에 붙어있으면 읽기 가능해짐
# 읽기 계열에 붙어있으면 쓰기 가능해짐

# 문제
# 파일 처리
# 단어 중 대소문자 구분없이 c를 포함하는 단어를 출력하시오. 단 , . 은 출력하지 마시오

a = "abc def"
aArr = str(a.split())
# print(aArr)
# print(aArr.find("c"))

quizAnswer = []
with open("word.txt", "r") as quizFile:
    quizAllText = quizFile.read()
    quizTextArr = quizAllText.split(" ")
    for i in range(len(quizTextArr)):
        # print(quizTextArr[i]) # 출력 테스트
        cIndex = quizTextArr[i].lower().find("c")
        # print(quizTextArr[i].find("c")) # 출력 테스트
        # print(cIndex)
        if cIndex != -1:
            # quizAnswer += str(quizTextArr[cIndex])
            # quizAnswer += quizTextArr[i]
            quizAnswer.append(quizTextArr[i].strip(",").strip("."))
for item in quizAnswer:
    print(item)
# print(quizAnswer, end="\n")
# print(quizTextArr)
# print(quizAllText)

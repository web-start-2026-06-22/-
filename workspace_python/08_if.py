a = 10
b = 5
print(3 < a < 20)

if True:
    print(1)
    # print(2)
    print(3)

    if True:
        print(4)
if True:
    pass
else:
    pass

if 1:
    print("참")

"""
파이썬에서 false란?
false, None, 0, 0.0, 빈 컨테이너(비어있는 문자열, 리스트, 튜플, 딕셔너리)
"""

a = []
if a:
    print("참")
else:
    print("거짓")

score = input("점수 4개 입력, 띄어쓰기로 구분. 0부터 100까지의 값만 입력하세요.")
scores = score.split(" ")

if (
    (0 <= scores[0] <= 100)
    and (0 <= scores[1] <= 100)
    and (0 <= scores[2] <= 100)
    and (0 <= scores[3] <= 100)
):
    print("올바른 점수가 아닙니다.")
    sum = int(scores[0]) + int(scores[1]) + int(scores[2]) + int(scores[3])
    average = sum / len(scores)
    if average >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못된 입력")

button = int(input("1번: 콜라, 2번: 사이다, 3번: 환타"))

if button == 1:
    print("콜라")
elif button == 2:
    print("사이다")
elif button == 3:
    print("환타")
else:
    print("유효하지 않은 메뉴")

# break 필요 없음
# 또는은 | (파이프)

a = "여름"
match a:
    case "봄":
        print("봄")
    case "여름":
        print("여름")
    case "가을":
        print("가을")
    case "겨울":
        print("겨울")
    case _:
        print("이거 계절 아님")

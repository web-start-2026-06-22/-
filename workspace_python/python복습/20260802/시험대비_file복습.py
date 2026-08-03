# testText = input("상품명, 개수, 가격 순으로 입력하세요. 띄어쓰기로 구분합니다.").split()
# print(testText)

# with open("test.txt", "w") as file:
#     file.write(str(testText))
# print(str(testText))
# 여기까지 샘플 데이터 생성용

testArr = []
tempArr = []
testDict = {}
with open("test.txt", "r") as file:
    # file.read().replace("'", "")
    tempArr = file.read().replace("'", "")
    tempArr = tempArr.replace("[", "").replace("]", "").replace(",", "").split()
    print(tempArr)
    for i in range(len(tempArr)):
        # 여기부터
        # for i in range(0, len(tempArr), 3): # 이렇게 쓰면 좀 더 깔끔할 것.
        # 아래의 if i > 15: break, i % 3 == 0:을 제거해도 동작.
        # 여기까지 20260803
        # print(item)
        # print(tempArr[0])
        # index 3개 단위로 끊을 수 있는 방법이 없을까 이럴 땐 len(tempArr)가 적합하겠지.
        # print(i)
        # print(tempArr[i])
        if i > 15:
            break
        if i % 3 == 0:
            if (
                tempArr[i + 1].find("-") == -1 and tempArr[i + 2].find("-") == -1
            ) and tempArr[i + 2].find(
                "원"
            ) == -1:  # 이상치 제거
                testArr.append(
                    [tempArr[i], int(tempArr[i + 1]), int(tempArr[i + 2])]
                )  # 배열로 만들기
                testDict[tempArr[i]] = (
                    int(tempArr[i + 1]),
                    int(tempArr[i + 2]),
                )  # 딕셔너리로 만들기

print(testArr)
print(testDict)
# print(testDict.keys())
testSum = 0
testMaxSalesItem = ""  # 가장 많이 팔린 상훔명
testMaxSales = 0  # 가장 많이 팔린 상품 팔린 개수
testMax = 0  # 가장 높은 매출
testMaxItem = ""  # 가장 높은 매출 상명명
for i in testDict:
    # print(i)
    # print(testDict[i])
    # print(type((testDict[i][0])))
    # print(testDict[i][0] * testDict[i][1])
    if testMaxSales < testDict[i][0]:
        testMaxSalesItem = i
        testMaxSales = testDict[i][0]
    testSum += testDict[i][0] * testDict[i][1]
    if testMax < testDict[i][0] * testDict[i][1]:
        testMaxItem = i
        testMax = testDict[i][0] * testDict[i][1]
print("총 매출:", testSum, "원")
print("가장 많이 팔린 상품:", testMaxSalesItem, f"({testMaxSales}개)")
print("매출이 가장 높은 상품:", testMaxItem, f"({testMax}원)")

# 담을 때 int 처리가 훨씬 낫다.

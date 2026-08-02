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
                    [tempArr[i], tempArr[i + 1], tempArr[i + 2]]
                )  # 배열로 만들기
                testDict[tempArr[i]] = (
                    tempArr[i + 1],
                    tempArr[i + 2],
                )  # 딕셔너리로 만들기

print(testArr)
print(testDict)
# print(testDict.keys())
testSum = 0
testMaxSalesItem = ""
testMaxSales = 0
testMax = 0
testMaxItem = ""
for i in testDict:
    # print(i)
    # print(testDict[i])
    # print(type((testDict[i][0])))
    print(int(testDict[i][0]) * int(testDict[i][1]))
    if len(testMaxSalesItem) < int(testDict[i][0]):
        testMaxSalesItem = i
        testMaxSales = testDict[i][0]
    testSum += int(testDict[i][0]) * int(testDict[i][1])
    if testMax < int(testDict[i][0]) * int(testDict[i][1]):
        testMaxItem = i
        testMax = int(testDict[i][0]) * int(testDict[i][1])
print("총 매출:", testSum, "원")
print("가장 많이 팔린 상품:", testMaxSalesItem, f"({testMaxSales}개)")
print("매출이 가장 높은 상품:", testMaxItem, f"({testMax}원)")

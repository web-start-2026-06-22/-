tempArr = []
temp2dArr = []
testDict = {}
sum = 0
with open("order.txt", "r", encoding="utf-8") as file:
    tempArr = file.read()

    tempArr = tempArr.split("\n")

    for item in tempArr:
        if item.find("-") == -1 and item.find("원") == -1:  # 이상치 제거
            temp2dArr = item.replace(",", "").split()
            if int(temp2dArr[2]) < 10000:
                testDict[temp2dArr[0]] = {temp2dArr[1], temp2dArr[2]}
                sum += int(temp2dArr[1]) * int(temp2dArr[2])

# for i in range(0, len(temp2dArr), 3):
# testDict[temp2dArr[i]] = (temp2dArr[i + 1], temp2dArr[i + 2])
# print(testDict)
print("전체 매출:", sum)

# 구구단

'''
형식?
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
...
9 * 9 = 81
'''

# print('2 * 1 = 2')
# print('2 * 2 = 4')
# print('2 * 3 = 6')

# 앞의 숫자, 단이 변경(증가)되는 것은 뒤의 숫자가 9까지 진행됐을 때.

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = ', i * j)
        
# 람다 섞어보기.
# for i in range(2, 10):
#     lambda x=i: x * (range(1, 10))
# 근데 잘 감이 안 잡히네.
# 2단만 우선 출력해보기.

gugu =lambda x : [x * y for y in range(1,10)]

# what_dan = int(input('출력 시작할 단수를 입력하세요:'))

# lambda dan=2 
# 기본값을 2로 주겠다.
gugu_renew = lambda dan=2: [[dan * num for num in range(1,10) ] for dan in range(what_dan, 10)]
# print(gugu(2))

# for i in range(2, 10):
#     print(gugu(i))
    
# print(gugu_renew(what_dan), '\n')
# print(gugu_renew(), '\n')

print('-'*30)

# 3단씩 가로로 출력
'''
2 * 1 = 2 3 * 1 = 3 4 * 1 = 4
2 * 2 = 4 3 * 2 = 6 4 * 2 = 8
2 * 3 = 6 3 * 3 = 9 4 * 3 = 12
...

8 * 9 = 72 9 * 9 = 81
마지막 10은 출력하지 않는다.
'''

# print('2 * 1 = 2, 3 * 1 = 3, 4 * 1 = 4')
# print('2 * 2 = 4, 3 * 2 = 6, 4 * 2 = 8')
# print('2 * 3 = 6, 3 * 3 = 9, 4 * 3 = 12')

# for i in range(2, 10, 3):
#     for j in range(1, 10):
#         if i+2 < 10:
#             print(f"{i} * {j} = {i*j}, {i+1} * {j} = {(i+1) * j}, {i+2} * {j} = {(i+2) * j}")
#         else:
#             print(f"{i} * {j} = {i*j}, {i+1} * {j} = {(i+1) * j}")
            
            
# pyramid

"""
            ____+____
            ___+++___
            __+++++__
            _+++++++_
            +++++++++
"""

# print('____*____') # 별 1개
# print('___***___') # 별 3개
# print('__*****__') # 별 5개
# print('_*******_') # 별 7개
# print('*********') # 별 9개

# 즉 라인당 별 개수는 2n-1개.
# 1부터 시작한다면 2n-1,
# 끝나는 숫자는 +1 왜? range(시작인덱스, 종료인덱스)라면 시작~종료-1까지
# 0부터 시작한다면 2n+1

# for i in range(1, 6):
#     print('*'*5) # 이러면 ***** 5줄 출력

# 문자열 +는 이어붙이기가 되므로
for i in range(1, 6):
    print('_'*(5-i)+'*'*(2 * i -1)+'_'*(5-i))
    
# 변수로 조절
start=int(input('출력을 시작할 줄 번호 입력:'))    
end=int(input('출력을 끝낼 줄 번호 입력:'))    
for i in range(start, end+1):
    print('_'*(end-i)+'*'*(2 * i -1)+'_'*(end-i))
todo_list = []

d1 = {
    'id': 14692,
    'item': 'item1'
}

# Create
# d1을 리스트에 추가
todo_list.append(d1)
print(todo_list)

d2 = {
    'id': 29681,
    'item': 'item2'
}

todo_list.append(d2)
print(todo_list)

# Read
# id가 29681인 것의 모든 딕셔너리 출력
# print(todo_list[1])
for item in todo_list:
    if item.get('id') == 29681:
        print(item)

# Update
# id가 29681인 것의 item을 '아이템2'로 바꾼뒤 todo_list 출력
for item in todo_list:
    if item.get('id') == 29681:
        item['item'] = '아이템2'
print(todo_list)

# Delete
# id가 29681인 것의
# index를 찾아내고
# pop으로 해당 index를 지운다.
for i in range(len(todo_list)):
    print('i', i)
    if todo_list[i].get('id') == 29681:
        todo_list.pop(i)
        break
print(todo_list)

todo_list2 = [ todo for todo in todo_list if todo['id'] != 29681 ]
print('-'*30)
print(todo_list2)

# crud.py
# todo_list에 CRUD하는 라우터를 설정하고
# api.py를 실행해서 테스트하기

# 이케이케 해도 되고
# /todo/c
# /todo/r
# /todo/u
# /todo/d

# 이렇게 할 수 있을까요?
# /crud [GET, POST, PUT, DELETE]
from fastapi import APIRouter, Request
from todo import todo_list
from model import Todo

# crud_router = APIRouter()
crud_router = APIRouter()

@crud_router.get('/crud/r')
def read_todoList():
    print('crud read 실행')
    print(todo_list)
    return todo_list
# async def read_todo(id : int) -> dict:
#     for item in todo_list:
#         if item.id == id:
#             print(item)
#             return item
#     return todo_list

@crud_router.post('/crud/c')
async def create_todo(todo : Todo) -> dict:
    todo_list.append(todo)
    print('crud create 실행')
    print(todo_list)
    return {
        'message': '정상적으로 추가되었습니다.'
    }
    
@crud_router.put('/crud/u') # todo_list의 변경할 값을 추가로 전달 인자로 받아주기.
async def update_todo(id : int, item : str) -> dict:
    for todo in todo_list:
        if todo.id == id:
            print(todo)
            return(todo)

@crud_router.delete('/crud/d') # todo_list의 어떤 값을 삭제할지 전달 인자로 받아주기.
async def delete_todo(id : int):
   todo_list = [ todo for todo in todo_list if todo['id'] != id ]
   print(todo_list)
   return(todo_list)
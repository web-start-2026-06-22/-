from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from todo import Todo

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

todo_list = []

@app.get('/todolist')
def read_list(request: Request):
    print('/todolist 실행 성공')
    return templates.TemplateResponse(
        request,
        "todolist.html",
        {
            'read_list': todo_list # dict의 key값이 html로 던져주고 html에서 사용할 변수명
        }
    )

@app.get('/add')
def add(request: Request):
    print('/add 실행 성공')
    return templates.TemplateResponse(
            request,
            "addlist.html"
        )
    
@app.get('/detail/{id}')
def detail(request: Request, id:int):
    print('/detail/{id} 실행 성공')
    print('id:', id)
    
    result = None
    for todo in todo_list:
            if todo.id == id:
                result = todo
                
    return templates.TemplateResponse(
            request,
            "list_detail.html",
            {
                'todo': result
            }
        )

@app.get('/updatelist')
def updatelist(request: Request, id:int):
    print('/updatelist 실행 성공')
    print('id', id)
    
    result = None
    for todo in todo_list:
        if todo.id == id:
            result = todo
                    
    return templates.TemplateResponse(
        request,
        "updatelist.html",
            {
                'todo': result
            }
    )

@app.post('/api/add')
def addlist(todo: Todo = Form()):
    print('/api/add 실행 성공')
    print('todo:', todo)
    
    todo_list.append(todo)
    
    return RedirectResponse(
            url='/todolist',
            status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다.
        )
    
@app.post('/api/update')
def updatelist(todo: Todo = Form()):
    print('/api/update 실행 성공')
    print('todo:', todo)
    
    for record in todo_list:
        if record.id == todo.id:
            record.item = todo.item
    
    return RedirectResponse(
            url='/todolist',
            status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다.
        )
    
@app.post('/api/delete')
def deletelist(todo: Todo = Form()):
    print('/api/delete 실행 성공')
    print('todo:', todo)
    
    for i in range(len(todo_list)) :
        print('i', i)
        if todo_list[i].id == todo.id:
            todo_list.pop(i)
            break
    
    return RedirectResponse(
            url='/todolist',
            status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다.
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True)
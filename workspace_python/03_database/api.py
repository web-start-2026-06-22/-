from sqlmodel import create_engine, Session, SQLModel
from fastapi import FastAPI, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from sqlalchemy import text

from DTO.EmpDTO import Emp3
from DTO.DeptDTO import Dept3

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

emp_list = []

DATABASE_URL = 'mysql+pymysql://root:human1234$@127.0.0.1:3306/human'

engine = create_engine(DATABASE_URL,echo=True)

def get_session():
    with Session(engine) as session :
        yield session
        session.commit()

@app.get('/emplist')
def emp_list_deptno(
    request:Request,
    session:Session = Depends(get_session)
):
    print('/emplist 실행 성공')      
    try:
        # text : sql문을 실행하기 전에 미리 컴파일 해둔다.
        sql = text('''
            select *
            from emp3
        ''')
        
        result = session.execute(sql)
        emp_list = result.mappings().fetchall()
        # print(emp_list)
        
    except Exception as e:
        print(e)
    
    return templates.TemplateResponse(request, "emplist.html", {
                'emp_list': emp_list
            })

@app.get('/empadd')
def empadd(
    request: Request,
    session:Session = Depends(get_session)
    ):
    print('/empadd 실행 성공')
    sql = text('''
               select deptno, dname
               from dept3
               ''')
    result = session.execute(sql)
    dept_list = result.mappings().fetchall()
    return templates.TemplateResponse(
            request,
            "empadd.html",
            {
                'dept_list': dept_list
            }
        )
    
@app.get('/detail/{empno}')
def detail(
    request: Request,
    empno:int,
    session:Session = Depends(get_session)
    ):
    print('/detail/{empno} 실행 성공')
    print('empno:', empno)
    
    sql = text('''
               select * from emp3
               where empno = :empno
               ''')
    
    result = session.execute(sql, {'empno': empno})
    detail_emp = result.mappings().fetchone()
    
    return templates.TemplateResponse(
            request,
            "empdetail.html",
            {
                'emp': detail_emp
            }
        )
    
@app.get('/empupdate')
def empupdate(
    request:Request,
    empno: int,
    session:Session = Depends(get_session)
    ):
    print('/empupdate 실행 성공')
    # print('empno:', empno)
    
    sql = text('''
                   select * from emp3
                   where empno = :empno
                   ''')
    
    sql2 = text('''
                select deptno, dname
                from dept3
                ''')
        
    result = session.execute(sql, {'empno': empno})
    update_emp = result.mappings().fetchone()
    
    result2 = session.execute(sql2)
    dept_list = result2.mappings().fetchall()
        
    return templates.TemplateResponse(
        request,
        "empupdate.html",
            {
                'emp': update_emp,
                'dept': dept_list
            }
    )
    
@app.post('/api/add')
def addlist(
    emp: Emp3 = Form(),
    session:Session = Depends(get_session)
    ):
    print('/api/add 실행 성공')
    print('emp:', emp)
    
    addData = dict(emp)
    
    sql = text('''
               insert into emp3
               values ( :empno, :ename, :job, :mgr, :hierdate, :sal, :comm, :deptno)
               ''')
    
    session.execute(sql, addData)
    
    # emp_list.append(emp)
    
    return RedirectResponse(
            url='/emplist',
            status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다.
        )

@app.post('/api/update')
def updatelist(
    emp: Emp3 = Form(),
    session:Session = Depends(get_session)
    ):
    print('/api/update 실행 성공')
    print('emp:', emp)
    
    result = dict(emp)
    
    sql = text('''
               update emp3
               set ename = :ename,
               job = :job,
               mgr = :mgr,
               hierdate = :hierdate,
               sal = :sal,
               comm = :comm,
               deptno = :deptno
               where empno = :empno
               ''')
    
    # session.execute(sql, {'ename': emp.ename, 
    #                       'job': emp.job,
    #                       'mgr': emp.mgr,
    #                       'hierdate': emp.hierdate,
    #                       'sal': emp.sal,
    #                       'comm': emp.comm,
    #                       'deptno': emp.deptno,
    #                       'empno': emp.empno})
    
    session.execute(sql, result)
    
    return RedirectResponse(
            url='/emplist',
            status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다.
        )

@app.post('/api/delete')
def deletelist(
    empno: int = Form(),
    session:Session = Depends(get_session)
    ):
    print('/api/delete 실행 성공')
    print('empno:', empno)
    
    sql = text('''
               delete from emp3
               where empno = :empno
               ''')
    
    session.execute(sql, {'empno': empno})
    
    return RedirectResponse(
                url='/emplist',
                status_code=303 # 303: 무조건 GET으로 다시 들어오게 한다.
            )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True)
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/hello")
def hello(request: Request):
    print("/hello 실행")
    return templates.TemplateResponse(request, "home.html", {
        'ip': request.client.host,
        'msg': '안뇽?'
    })

# 서버에서 보낸 변수로 html에서 중괄호, 퍼센트 이용해서 if 처리 가능
@app.get("/youtube")
def youtube(request: Request):
    print("/youtube 실행")
    # 템플릿 레이아웃을 상속받아 실제로 컨텐츠 영역을 구현하는 html 파일을 지정해줌.
    return templates.TemplateResponse(request, "youtube.html", {
        'like': '55만',
        'star': 4,
        'bookmark': ['동영상1', '동영상2', '동영상3', '동영상4', '동영상5']
        
    })

def price(value) :
    return f'{int(value):,}'
# 사용자 필터 만들고 적용하기
# ['price'] : Jinja에서 사용할 필터 이름
templates.env.filters['price'] = price

# 날짜 포맷
from datetime import datetime
def format_date(value, format="%Y-%m-%d %H:%M:%S"):
    v = datetime.fromisoformat(value)
    return v.strftime(format)
templates.env.filters['format_date'] = format_date

# textarea의 엔터 문자인 \n을 <br>로 바꾸고 HTML로 인식 시키는 필터

def n2br(value):
    from markupsafe import Markup # innerHTML로 만들어 주는 모듈
    return Markup(value.replace('\n', '<br>'))
templates.env.filters['n2br'] = n2br

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", port=8000, reload=True)

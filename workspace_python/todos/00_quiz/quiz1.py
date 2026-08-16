from fastapi import FastAPI

# 서버 키기
q1_app = FastAPI()

@q1_app.get('/dan')
async def print_dan(dan : int):
    print([dan * i for i in range(1, 10)])




if __name__ == "__main__":
    import uvicorn
    uvicorn.run("quiz1:q1_app", port=8000, reload=True)
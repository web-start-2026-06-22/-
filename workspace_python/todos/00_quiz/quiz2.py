from fastapi import FastAPI

q2_app = FastAPI()

@q2_app.get('/q2')
def q2_add(num1: int, num2: int):
    print(num1 + num2)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("quiz2:q2_app", port=8000, reload=True)
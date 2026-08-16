from fastapi import FastAPI

q3_app = FastAPI()


@q3_app.get("/q3")
def q3_op(num1: int, num2: int, op):
    if op == "+":
        print(num1 + num2)
        return num1 + num2
    elif op == "*":
        print(num1 * num2)
        return num1 * num2
    elif op == "**":
        print(num1**num2)
        return num1**num2
    elif op == "/":
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
            return "0으로 나눌 수 없습니다."
        print(num1 / num2)
        return num1 / num2
    elif op == "//":
        if num2 == 0:
            print("0으로 나눌 수 없습니다.")
            return "0으로 나눌 수 없습니다."
        print(num1 // num2)
        return num1 // num2
    elif op == "%":
        print(num1 % num2)
        return num1 % num2


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("quiz3:q3_app", port=8000, reload=True)

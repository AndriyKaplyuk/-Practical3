from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html", media_type="text/html")

@app.post("/postdata")
def postdata(number1: float = Form(), number2: float = Form(), act: str = Form()):  # Додаємо act у параметри
    if act == 'summ':
        result = number1 + number2
    elif act == 'minus':
        result = number1 - number2
    elif act == 'mult':
        result = number1 * number2
    elif act == 'div':
        if number2 == 0:
            return {"error": "Division by zero is not allowed"}
        result = number1 / number2
    else:
        return {"error": "Invalid operation"}

    return {"result": result}

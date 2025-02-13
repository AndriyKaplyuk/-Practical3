from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")


@app.post("/postdata")
def postdata(number1 = Form(), act = Form(), number2=Form()):
    n1 = float(number1)
    n2 = float(number2)

    if act == 'summ':
        result = n1 + n2
    elif act == 'minus':
        result = n1 - n2
    elif act == 'mult':
        result = n1 * n2
    elif act == 'div':
        result = n1 / n2
    else:
        result = 'Operation impossible'

    return {"result": result}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    nombres = "Leidy T"
    mensaje = f"hola a todos...atentamente {nombres}"
    return {"mensaje": mensaje}

@app.get("/suma")
async def suma(num1: float, num2: float):
    resultado = num1 + num2
    return {"operacion": "suma", "a": num1, "b": num2, "resultado": resultado}

@app.get("/resta")
async def resta(num1: float, num2: float):
    resultado = num1 - num2
    return {"operacion": "resta", "a": num1, "b": num2, "resultado": resultado}

@app.get("/multiplicacion")
async def suma(num1: float, num2: float):
    resultado = num1 * num2
    return {"operacion": "suma", "a": num1, "b": num2, "resultado": resultado}

@app.get("/division")
async def suma(num1: float, num2: float):
    resultado = num1 / num2
    return {"operacion": "suma", "a": num1, "b": num2, "resultado": resultado}
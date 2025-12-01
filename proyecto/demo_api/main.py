# main.py
from fastapi import FastAPI
from demo_api.movies import router


# Crear la instancia de la app
app = FastAPI()

app.include_router(router)
app.title = "Ejmplos basicos"
app.version = "1.0.0"


# Endpoint de prueba
@app.get("/", tags=['basicos'])
async def read_root():
    nombres = "Leidy T"
    mensaje = f"hola a todos...atentamente {nombres}"
    return {"mensaje": mensaje}

@app.get("/saludos", tags=['basicos'])
async def saludos():
    return{"mensaje": "HOLA A TODOS"}


@app.get("/suma", tags=['basicos'])
async def get_suma(num1:int, num2:int):

    """
    Esto es una suma simple 
    """
    res = num1 + num2
    return{"suma": res}

@app.get("/mult/{num1}/{num2}", tags=['basicos'])
async def get_mult(num1:int, num2:int):
    """
    El metodo realiza una multiplicacion, los paramentros...etc. 
    """

    resultado = num1 * num2
    return{"resultado": resultado}

@app.get("/operacion/{num1}/{num2}", tags=['basicos'])
async def get_operacion(tipo, num1:int, num2:int):
    """
    El metodo realiza una multiplicacion, los paramentros...etc. 
    """

    resultado = 0
    match tipo:
        case "SUM   A":
            resultado = num1 + num2
        case "RESTA":
            resultado = num1 - num2
        case "MULTI":
            resultado = num1 * num2
        case _:
            resultado = "Operacion no reconocida"

    return{"resultado": resultado}


@app.post("/registrar/{provincia}", tags=['basicos'])
async def registrar(provincia, cantones:dict):
    """
    METODO POST
    """
    return{"provincia": provincia, "cantones":cantones}


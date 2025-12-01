from fastapi import FastAPI
from demo_api.routers.movie_router import router as movie_router 
from demo_api.routers.fraccion_router import router_fraccion

app = FastAPI()

app.title = "Ejmplos basicos"
app.version = "1.0.0"

app.include_router(prefix="/v1", router=router) 
app.include_router(router_fraccion)




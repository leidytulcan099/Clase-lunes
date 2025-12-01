import datetime
from fastapi import APIRouter, FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import List, Literal, Optional

app = FastAPI()
router = APIRouter()

# Modelo de película
class Movie(BaseModel):
    id: int
    nombre: str = Field(..., min_length=3, max_length=100)
    categoria: Literal["accion", "comedia", "drama"]
    año: int = Field(..., le=datetime.date.today().year, ge=1900)

# Base de datos inicial
movies_array = [
    {"id": 1, "nombre": "Pelicula 1", "categoria": "accion", "año": 2025},
    {"id": 2, "nombre": "Pelicula 2", "categoria": "comedia", "año": 2023}
]

# GET todas las películas
@router.get("/movies", response_model=List[Movie], tags=['peliculas'])
async def get_movies() -> List[Movie]:
    return [Movie(**m) for m in movies_array]

# POST nueva película
@router.post("/movies", response_model=Movie, tags=['peliculas'])
async def create_movies(movie: Movie) -> Movie:
    for m in movies_array:
        if m["id"] == movie.id:
            raise HTTPException(status_code=400, detail="Ya existe una película con este ID")
    movies_array.append(movie.model_dump())  # Guardar como dict
    return movie

# PUT / update película
@router.put("/movies", response_model=Movie, tags=['peliculas'])
async def update_movies(movie: Movie) -> Movie:
    for index, m in enumerate(movies_array):
        if m["id"] == movie.id:
            movies_array[index] = movie.model_dump()
            return movie
    raise HTTPException(status_code=404, detail="La película no existe")

# DELETE película por ID
@router.delete("/movies/{id}", response_model=Movie, tags=['peliculas'])
async def delete_movies(id: int = Path(gt=0)) -> Movie:
    for index, m in enumerate(movies_array):
        if m["id"] == id:
            pelicula_eliminada = movies_array.pop(index)
            return Movie(**pelicula_eliminada)
    raise HTTPException(status_code=404, detail="La película no existe")

# GET /movies/search
@router.get("/movies/search", response_model=List[Movie], tags=['peliculas'])
async def search_movies(
    anio: Optional[int] = Query(None, gt=1900),
    categoria: Optional[str] = Query(None, min_length=3)
) -> List[Movie]:
    resultados = movies_array
    if anio is not None:
        resultados = [m for m in resultados if m["año"] == anio]
    if categoria is not None:
        resultados = [m for m in resultados if m["categoria"].lower() == categoria.lower()]
    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron películas con los criterios proporcionados")
    return [Movie(**m) for m in resultados]

# Incluir router en app
app.include_router(router)







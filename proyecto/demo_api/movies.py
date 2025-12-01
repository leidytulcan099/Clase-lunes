from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
#distanciamiento
router = APIRouter()

# Creacion de clase para enviar datos
class Movie(BaseModel):
    id: int
    nombre : str
    categoria: str
    año: int

movies_array = {
    {
         'id' : 1,
     'nombre' : 'Pelicula 1',
     'categoria' : 'accion',
     'año' : 2025
    },
    {
         'id' : 2,
        'nombre' : 'Pelicula 2',
        'categoria' : 'comedia',
        'año': 2023
    }
}

@router.get("/movies", tags=['peliculas'])
async def get_movies():
   return movies_array 

@router.post("/movies", tags=['peliculas'])
async def create_movies(movie: Movie):
    for m in movies_array:
        if m["id"] == movie.id:
            raise HTTPException(
                status_code=400,
                detail="Ya existe una pelicula con este ID"
            )
    
    nueva_pelicula = movie.model_dump()
    movies_array.append(nueva_pelicula)

    return {
        "mensaje": "Pelicula agregada exitosamente",
        "pelicula": nueva_pelicula
    }

@router.delete("/movies", tags=['peliculas'])
async def delete_movies(movie: Movie):
    for index, m in enumerate(movies_array):
        if m["id"] == movie.id:
            movies_array[index] = movie.model_dump()
            return {
                "mensaje": "Película actualizada",
                "pelicula": movies_array[index]
            }

   
    raise HTTPException(status_code=404, detail="La película no existe")


@router.delete("/movies/{id}", tags=['peliculas'])
async def delete_movies(id: int):
    for index, m in enumerate(movies_array):
        if m["id"] == id:
            pelicula_eliminada = movies_array.pop(index)
            return {
                "mensaje": "Película eliminada exitosamente",
                "pelicula": pelicula_eliminada
            }

    raise HTTPException(status_code=404, detail="La película no existe")

@router.get("/movies/search", tags=['peliculas'])
async def search_movies(año: int, categoria: str):
    result = []
    for m in(movies_array):
        if m["año"] == año and m["categoria"] == categoria:
            result.append(m)

    return result 


@router.get("/movies/search", tags=['peliculas'])
async def search_movies(anio: Optional[int] = None,
                        categoria: Optional[str] = None):
    resultados = movies_array

    if anio is not None:
        resultados = [m for m in resultados if m["año"] == anio]

    if categoria is not None:
        resultados = [m for m in resultados if m["categiria"].lower() == categoria.lower()]

    if anio is not None and categoria is not None:
        resultados = [m for m in resultados if m["año"] == anio and m["categoria"].lower() == categoria.lower()]

    if not resultados:
        raise HTTPException(status_code=404, detail="No se encontraron peliculas con los criterios proporcionados")
    
    return resultados


      






from data_base import tabla, agregar_fila, agregar_varios, actualizar, seleccionar, eliminar_fila
from modelos import Peli, Ides, Tabla
from fastapi import APIRouter
from fastapi import HTTPException

router = APIRouter()

@router.post("/", response_model=Ides)
def movie_add(pelicula:Peli):
    try:
        add = agregar_fila(pelicula.title, pelicula.director, pelicula.year)
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e)) 
    return Ides(mensaje=f"Pelicula agregada, la ID es: {add}")

@router.patch("/")
def update_movie(columna, dato, ide):
    try:
        actualizar(columna, dato, ide)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return{"Server message":"Fila actualizada"}

@router.get("/")
def select_movies(columna, valor):
    try:
        resultado = seleccionar(columna, valor)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return resultado

@router.delete("/")
def movie_delete(pelicula:Peli):
    try:
        eliminar_fila(pelicula.title, pelicula.director, pelicula.year)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=str(e))
    return{"Server message":"Pelicula eliminada"}
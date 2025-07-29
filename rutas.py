from data_base import tabla, agregar_fila, agregar_varios, actualizar, seleccionar, eliminar_fila
from modelos import Peli, Ides, Tabla
from fastapi import APIRouter, Query
from fastapi import HTTPException

router = APIRouter()

@router.post("/add", response_model=Ides)
def movie_add(pelicula:Peli):
    try:
        add = agregar_fila(pelicula.title, pelicula.director, pelicula.year)
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e)) 
    return Ides(mensaje=f"Pelicula agregada, la ID es: {add}")

@router.patch("/update")
def update_movie(columna: str = Query(...), dato: str = Query(...), ide: int = Query(...)):
    try:
        actualizar(columna, dato, ide)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return{"Server message":"Fila actualizada"}

@router.get("/select")
def select_movies(columna: str = Query(...), valor: str = Query(...)):
    try:
        resultado = seleccionar(columna, valor)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return resultado

@router.delete("/delete")
def movie_delete(pelicula:Peli):
    try:
        eliminar_fila(pelicula.title, pelicula.director, pelicula.year)
    except Exception as e:  
        raise HTTPException(status_code=404, detail=str(e))
    return{"Server message":"Pelicula eliminada"}
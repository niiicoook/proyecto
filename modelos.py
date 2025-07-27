from pydantic import BaseModel, Field
from typing import Optional

class Peli(BaseModel):
    title: str = Field(..., min_length=1)
    director: Optional[str] = Field(None, min_length=1)
    year: int = Field(..., ge= 1895, le=2025)

class Ides(BaseModel):
    mensaje: str

class Tabla(BaseModel):
    nombre: str
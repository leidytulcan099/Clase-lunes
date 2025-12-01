import datetime
from typing import Literal
from pydantic import BaseModel, Field, field_validator


class Movie(BaseModel):
    id: int
    nombre: str = Field(..., min_length=3, max_length=100)
    categoria: Literal["accion", "comedia", "drama"]
    año: int = Field(..., le=datetime.date.today().year, ge=1900)


    @field_validator('nombre')
    def validate_name(cls, value):
        if len(value) < 3 or len(value) > 100:
            raise ValueError("el nombre debe tener mas de 3 caracteres y menos de 100")
        return value
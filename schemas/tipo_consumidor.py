from pydantic import BaseModel

class TipoConsumidorCreate(BaseModel):
    nome: str
    valor_kwh: float

class TipoConsumidorUpdate(BaseModel):
    nome: str
    valor_kwh: float

class TipoConsumidorRead(BaseModel):
    id: int
    nome: str
    valor_kwh: float

class TipoConsumidorReadList(BaseModel):
    tipos_consumidores: list[TipoConsumidorRead]

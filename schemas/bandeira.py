from pydantic import BaseModel

class BandeiraCreate(BaseModel):
    nome: str
    tarifa: float

class BandeiraRead(BaseModel):
    id: int
    nome: str
    tarifa: float

class BandeiraUpdate(BaseModel):
    nome: str
    tarifa: float

class BandeiraReadList(BaseModel):
    bandeiras: list[BandeiraRead]

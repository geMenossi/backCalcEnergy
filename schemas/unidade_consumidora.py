from pydantic import BaseModel
from schemas.dependencia import DependenciaReadMany

class UnidadeConsumidoraCreate(BaseModel):
    nome: str
    tipo_id: int

class UnidadeConsumidoraUpdate(BaseModel):
    nome: str

class UnidadeConsumidoraRead(BaseModel):
    id: int
    nome: str
    tipo_id: int
    dependencias: list[DependenciaReadMany]

class UnidadeConsumidoraReadForList(BaseModel):
    id: int
    nome: str
    tipo_id: int

class UnidadeConsumidoraReadList(BaseModel):
    unidades_consumidoras: list[UnidadeConsumidoraReadForList]

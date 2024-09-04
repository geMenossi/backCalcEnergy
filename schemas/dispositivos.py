from pydantic import BaseModel, Field

class DispositivoCreate(BaseModel):
    unidade_consumidora_id: int
    dependencia_id: int
    tipo_id: int
    nome: str
    consumo: float = Field(gt=0)
    uso_diario: float = Field(ge=0, le=24)

class DispositivoUpdate(BaseModel):
    nome: str
    consumo: float = Field(gt=0)
    uso_diario: float = Field(ge=0, le=24)
    tipo_id: int

class DispositivoRead(BaseModel):
    id: int
    unidade_consumidora_id: int
    dependencia_id: int
    tipo_id: int
    nome: str
    consumo: float
    uso_diario: float

class DispositivoReadMany(BaseModel):
    id: int
    nome: str
    tipo_id: int

class DispositivoReadList(BaseModel):
    dispositivos: list[DispositivoReadMany]

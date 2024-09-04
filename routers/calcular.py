from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal
from models.tipo_consumidor import TipoConsumidorDB
from models.unidade_consumidora import UnidadeConsumidoraDB
from models.dependencia import DependenciaDB
from models.dispositivo import DispositivoDB
from models.bandeira import (BandeiraDB)

router = APIRouter(prefix='/calcular', tags=['CALCULAR'])


class CalculoRequest(BaseModel):
    tipo_consumidor_id: int
    unidade_consumidora_id: int
    dependencias_ids: list[int]
    dispositivos: list[dict]
    bandeira_id: int
    periodo: Literal['diario', 'mensal', 'anual']


class CalculoResponse(BaseModel):
    consumo_total: float
    custo_total: float


@router.post("/calcular", response_model=CalculoResponse)
async def calcular_energetico(request: CalculoRequest):
    if request.periodo == 'diario':
        consumo_total = calcular_consumo_diario(request)
        custo_total = calcular_custo_diario(consumo_total, request.bandeira_id)
    elif request.periodo == 'mensal':
        consumo_total = calcular_consumo_mensal(request)
        custo_total = calcular_custo_mensal(consumo_total, request.bandeira_id)
    elif request.periodo == 'anual':
        consumo_total = calcular_consumo_anual(request)
        custo_total = calcular_custo_anual(consumo_total, request.bandeira_id)
    else:
        raise HTTPException(status_code=400, detail="Período inválido")

    return CalculoResponse(
        consumo_total=consumo_total,
        custo_total=custo_total
    )


def obter_tipo_consumidor(tipo_consumidor_id: int):
    return TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)


def obter_unidade_consumidora(unidade_consumidora_id: int):
    return UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)


def obter_dependencias(dependencias_ids: list[int]):
    return DependenciaDB.select().where(DependenciaDB.id.in_(dependencias_ids))


def obter_dispositivos(dispositivos: list[dict]):
    dispositivos_db = []
    for dispositivo in dispositivos:
        dispositivos_db.append(DispositivoDB.get_or_none(DispositivoDB.id == dispositivo['id']))
    return dispositivos_db


def obter_bandeira(bandeira_id: int):
    return BandeiraDB.get_or_none(BandeiraDB.id == bandeira_id)


def calcular_consumo_diario(request: CalculoRequest) -> float:
    tipo_consumidor = obter_tipo_consumidor(request.tipo_consumidor_id)
    unidade_consumidora = obter_unidade_consumidora(request.unidade_consumidora_id)
    dependencias = obter_dependencias(request.dependencias_ids)
    dispositivos = obter_dispositivos(request.dispositivos)

    consumo_total = 0.0
    for dispositivo in dispositivos:
        consumo_total += dispositivo.consumo * dispositivo.uso_diario

    return consumo_total


def calcular_consumo_mensal(request: CalculoRequest) -> float:
    consumo_diario = calcular_consumo_diario(request)
    return consumo_diario * 30  # Assumindo 30 dias no mês


def calcular_consumo_anual(request: CalculoRequest) -> float:
    consumo_mensal = calcular_consumo_mensal(request)
    return consumo_mensal * 12  # Assumindo 12 meses no ano


def obter_tarifa_diaria(bandeira_id: int) -> float:
    bandeira = obter_bandeira(bandeira_id)
    return bandeira.tarifa_diaria if bandeira else 0.0


def obter_tarifa_mensal(bandeira_id: int) -> float:
    bandeira = obter_bandeira(bandeira_id)
    return bandeira.tarifa_mensal if bandeira else 0.0


def obter_tarifa_anual(bandeira_id: int) -> float:
    bandeira = obter_bandeira(bandeira_id)
    return bandeira.tarifa_anual if bandeira else 0.0


def calcular_custo_diario(consumo_total: float, bandeira_id: int) -> float:
    tarifa_diaria = obter_tarifa_diaria(bandeira_id)
    return consumo_total * tarifa_diaria


def calcular_custo_mensal(consumo_total: float, bandeira_id: int) -> float:
    tarifa_mensal = obter_tarifa_mensal(bandeira_id)
    return consumo_total * tarifa_mensal


def calcular_custo_anual(consumo_total: float, bandeira_id: int) -> float:
    tarifa_anual = obter_tarifa_anual(bandeira_id)
    return consumo_total * tarifa_anual


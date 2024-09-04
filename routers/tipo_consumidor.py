from fastapi import APIRouter
from models.tipo_consumidor import TipoConsumidorDB
from schemas.tipo_consumidor import (
    TipoConsumidorCreate, TipoConsumidorRead, TipoConsumidorReadList, TipoConsumidorUpdate
)

router = APIRouter(prefix='/tipos-consumidores', tags=['TIPOS DE CONSUMIDORES'])

@router.post(path='', response_model=TipoConsumidorRead)
def criar_tipo_de_consumidor(novo_tipo: TipoConsumidorCreate):
    tipo = TipoConsumidorDB.create(**novo_tipo.dict())
    return tipo

@router.get(path='', response_model=TipoConsumidorReadList)
def listar_tipos_de_consumidores():
    tipos = TipoConsumidorDB.select()
    return {'tipos_consumidores': [tipo for tipo in tipos]}

@router.get(path='/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def listar_tipo_de_consumidor(tipo_consumidor_id: int):
    tipo = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    return tipo

@router.patch(path='/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def atualizar_tipo_de_consumidor(tipo_consumidor_id: int, tipo_atualizado: TipoConsumidorUpdate):
    tipo = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    if tipo:
        tipo.nome = tipo_atualizado.nome
        tipo.valor_kwh = tipo_atualizado.valor_kwh
        tipo.save()
    return tipo

@router.delete(path='/{tipo_consumidor_id}', response_model=TipoConsumidorRead)
def excluir_tipo_de_consumidor(tipo_consumidor_id: int):
    tipo = TipoConsumidorDB.get_or_none(TipoConsumidorDB.id == tipo_consumidor_id)
    if tipo:
        tipo.delete_instance()
    return tipo

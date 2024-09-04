from fastapi import APIRouter
from models.dependencia import DependenciaDB
from models.dispositivo import DispositivoDB
from models.unidade_consumidora import UnidadeConsumidoraDB
from schemas.dispositivos import (
    DispositivoCreate, DispositivoRead, DispositivoReadList, DispositivoUpdate
)

router = APIRouter(prefix='/dispositivos', tags=['DISPOSITIVOS'])

@router.post(path='', response_model=DispositivoRead)
def criar_dispositivo(novo_dispositivo: DispositivoCreate):
    dispositivo = DispositivoDB.create(**novo_dispositivo.dict())
    return dispositivo

@router.get(path='/unidades-consumidoras/{unidade_consumidora_id}', response_model=DispositivoReadList)
def listar_dispositivos(unidade_consumidora_id: int):
    unidade_consumidora = UnidadeConsumidoraDB.get_or_none(UnidadeConsumidoraDB.id == unidade_consumidora_id)
    if unidade_consumidora:
        dispositivos = DispositivoDB.select().where(DispositivoDB.unidade_consumidora == unidade_consumidora)
        return {'dispositivos': [dispositivo for dispositivo in dispositivos]}
    return {'dispositivos': []}

@router.get(path='/dependencias/{dependencia_id}', response_model=DispositivoReadList)
def listar_dispositivos_por_dependencia(dependencia_id: int):
    dependencia = DependenciaDB.get_or_none(DependenciaDB.id == dependencia_id)
    if dependencia:
        dispositivos = DispositivoDB.select().where(DispositivoDB.dependencia == dependencia)
        return {'dispositivos': [dispositivo for dispositivo in dispositivos]}
    return {'dispositivos': []}

@router.get(path='/{dispositivo_id}', response_model=DispositivoRead)
def listar_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    return dispositivo

@router.patch(path='/{dispositivo_id}', response_model=DispositivoRead)
def atualizar_dispositivo(dispositivo_id: int, dispositivo_atualizado: DispositivoUpdate):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if dispositivo:
        dispositivo.nome = dispositivo_atualizado.nome
        dispositivo.consumo = dispositivo_atualizado.consumo
        dispositivo.uso_diario = dispositivo_atualizado.uso_diario
        dispositivo.tipo = dispositivo_atualizado.tipo
        dispositivo.save()
    return dispositivo

@router.delete(path='/{dispositivo_id}', response_model=DispositivoRead)
def eliminar_dispositivo(dispositivo_id: int):
    dispositivo = DispositivoDB.get_or_none(DispositivoDB.id == dispositivo_id)
    if dispositivo:
        dispositivo.delete_instance()
    return dispositivo

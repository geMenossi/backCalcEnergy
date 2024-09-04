from peewee import AutoField, CharField, ForeignKeyField, Model
from config.database import database
from models.unidade_consumidora import UnidadeConsumidoraDB

class DependenciaDB(Model):
    id = AutoField(column_name='dependencia_id')
    nome = CharField(column_name='dependencia_nome')
    unidade_consumidora = ForeignKeyField(
        column_name='dependencia_unidade_consumidora_id',
        model=UnidadeConsumidoraDB, backref='dependencias'
    )

    class Meta:
        database = database
        table_name = 'dependencias'

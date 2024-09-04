from peewee import AutoField, CharField, ForeignKeyField, Model
from config.database import database
from models.tipo_consumidor import TipoConsumidorDB

class UnidadeConsumidoraDB(Model):
    id = AutoField(column_name='unidade_consumidora_id')
    nome = CharField(column_name='unidade_consumidora_nome')
    tipo = ForeignKeyField(
        column_name='unidade_consumidora_tipo_id',
        model=TipoConsumidorDB,
        backref='unidades_consumidoras'
    )

    class Meta:
        database = database
        table_name = 'unidades_consumidoras'

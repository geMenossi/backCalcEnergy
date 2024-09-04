from peewee import AutoField, CharField, FloatField, Model
from config.database import database

class TipoConsumidorDB(Model):
    id = AutoField(column_name='tipo_consumidor_id')
    nome = CharField(column_name='tipo_consumidor_nome')
    valor_kwh = FloatField(column_name='tipo_consumidor_valor_kwh')

    class Meta:
        database = database
        table_name = 'tipos_consumidores'

from peewee import AutoField, CharField, FloatField, Model
from config.database import database

class BandeiraDB(Model):
    id = AutoField(column_name='bandeira_id')
    nome = CharField(column_name='bandeira_nome')
    tarifa = FloatField(column_name='bandeira_tarifa')

    class Meta:
        database = database
        table_name = 'bandeiras'

from peewee import CharField, IntegerField, Model
from database.database import db

class Pessoa(Model):
    nome = CharField()
    sobrenome = CharField()
    email = CharField()
    idade = IntegerField()
    data_nasc = CharField()
    
    class Meta:
        database = db
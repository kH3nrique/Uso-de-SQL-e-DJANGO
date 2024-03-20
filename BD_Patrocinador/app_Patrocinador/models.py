from django.db import models

class Patrocinador(models.Model):
    id_patrocinador = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    atividade = models.TextField(max_length=1000, default='Valor padrão')
    cnpj = models.IntegerField()
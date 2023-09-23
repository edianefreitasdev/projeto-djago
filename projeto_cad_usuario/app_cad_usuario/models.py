from django.db import models

class Usuario(models.Model):
    id_usuario=models.AutoField(primary_key=True)
    nome=models.TextField(max_length=300)
    idade=models.IntegerField()
    cpf=models.TextField(max_length=11, default='00000000000')

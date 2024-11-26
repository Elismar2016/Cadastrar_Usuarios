from django.db import models

# Crie o objeto que representa uma tabela no banco.
#

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField("max_Length=255")
    idade = models.IntegerField()
    

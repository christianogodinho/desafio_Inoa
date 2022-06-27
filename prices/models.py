from pyexpat import model
from django.db import models

# Create your models here.


class Price (models.Model):

    id = models.AutoField(primary_key=True)
    codigo = models.CharField(("Código"), max_length=150)
    stock = models.CharField(("Ação"), max_length=255)
    tipo = models.CharField(("Tipo"), max_length=150)
    qtd_Teorica = models.CharField(("Qtde. Teorica"), max_length=255)
    part = models.CharField(("Part.(%)"), max_length=150)

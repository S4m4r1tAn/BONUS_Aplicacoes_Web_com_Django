from django.db import models
from datetime import datetime
from djmoney.models.fields import MoneyField

'''
* investimento
* valor
* pago (true/false)
* data
'''

class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    #valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now())
    nome = models.CharField(max_length=100)
    valor = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
    
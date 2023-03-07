from django.db import models
from datetime import datetime
'''
* investimento
* valor
* pago
* data
'''


class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(default=datetime.now)

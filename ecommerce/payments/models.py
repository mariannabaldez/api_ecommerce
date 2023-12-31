from django.db import models

# Create your models here.
class Payment(models.Model):
    pedido = models.CharField(max_length=255)
    comprador = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    quantidade = models.IntegerField(default=0)
    forma_pagamento = models.CharField(
        max_length=10,
        choices=[
        ('credito', 'Credito'),
        ('debito', 'Debito'),
        ('boleto', 'Boleto')
        ]
    )
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Pedido #{self.pedido}"
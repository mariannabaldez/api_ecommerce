from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
  list_display = ("pedido", "item", "quantidade","data" )

admin.site.register(Payment, PaymentAdmin)
from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('payments/details/<int:id>', views.details, name='payments_details'),
]

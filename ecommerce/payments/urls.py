from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('payments/', views.payments, name='payments'),
    path('payments/details/<int:id>', views.details, name='payments_details'),
    path('testing/', views.testing, name='testing'),
]

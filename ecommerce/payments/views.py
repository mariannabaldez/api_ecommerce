from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Payment

def payments(request):
    all_payments = Payment.objects.all().values()
    template = loader.get_template('payments.html')
    context = {
        'all_payments': all_payments
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  order = Payment.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'payment': order,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],
  }
  return HttpResponse(template.render(context, request))

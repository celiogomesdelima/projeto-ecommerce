from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')

class SalvarPedido(View):
    pass

class Detalhe(View):
    pass
from django.shortcuts import render
from .models import Price
from django.http import HttpResponse
from datetime import datetime


def home(request):

    price_list = Price.objects.all()

    return render(request, 'prices/home.html',
                  {'price_list': price_list})

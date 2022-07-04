from django.shortcuts import render
from .models import Price
from .utils import get_plot


def home(request):

    price_list = Price.objects.all()
    x = [x.codigo for x in price_list]
    y = [y.qtd_Teorica for y in price_list]
    chart = get_plot(x, y)

    return render(request, 'prices/home.html',
                  {'chart': chart})

from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>')  # Quando usa text/html, está bugando.


# def trigger_error(request):
#     division_by_zero = 1 / 0  # noqa

from django.http import HttpResponse  # noqa
from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    return render(request, 'base/home.html')


# def trigger_error(request):
#     division_by_zero = 1 / 0  # noqa

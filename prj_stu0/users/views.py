from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    m = request.method

    if m == "GET":
        return render(request, 'login.html')
    else:
        return HttpResponse('Login')


def register(request):
    return HttpResponse('Register')
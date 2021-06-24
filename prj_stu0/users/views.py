from users.models import Students
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    m = request.method

    if m == "GET":
        return render(request, 'login.html')
    else:
        name = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')

        if name and pwd:
            c = Students.objects.filter(uname=name, upwd=pwd).count()
            if c == 1:
                return HttpResponse('Login Success')
        
        return HttpResponse('Login Failed')


def register(request):
    m = request.method

    if m == "GET":
        return render(request, 'register.html')
    else:
        name = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')

        if name and pwd:
            u = Students(uname=name, upwd=pwd)
            u.save()

            return HttpResponse('Register Success')
        
        return HttpResponse('Regsiter Failed')


def students(request):
    #* 1 get data from students table
    stus = Students.objects.all()

    return render(request, 'show.html', {'dics':stus})

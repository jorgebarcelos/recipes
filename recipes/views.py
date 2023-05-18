from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html', context={'msg': 'where is the icons?'})


def contact(request):
    return HttpResponse('<h1>Contact</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')

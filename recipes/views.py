from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/pages/home.html', context={'msg': 'where is the icons?'})


def recipes(request, id: int):
    return render(request, 'recipes/pages/recipe_view.html', context={'msg': 'where is the icons?'})

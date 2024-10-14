from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Category, Products


def index(request):

    categories = Category.objects.all()

    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
        "categories": categories
    }

    return render(request, 'main/index.html', context)




def about(request) -> HttpResponse:
     
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о чем-то '
    }

    return render(request, 'main/about.html', context)


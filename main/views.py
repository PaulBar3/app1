from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Магазин мебели HOME',
    }

    return render(request, 'main/index.html', context)




def about(request) -> HttpResponse:
     
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о чем-то '
    }

    return render(request, 'main/about.html', context)


# def contacts(request) -> HttpResponse:
     
#     context = {
#         'title': 'Home - Контакты',
#         'content': 'Баранавец - Красавец )))',
#         'content2': 'Дашка - сдобная ЛЯЖКА !!!!',
        
#     }

#     return render(request, 'main/contacts.html', context)
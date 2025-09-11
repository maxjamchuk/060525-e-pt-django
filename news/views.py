from django.http import HttpResponse
from django.shortcuts import render



info = {
    "users_count": 100600,
    "news_count": 1000,
    "menu": [
        {"title": "Главная",
         "url": "/"},
        {"title": "О проекте",
         "url": "/about/"},
        {"title": "Каталог",
         "url": "/news/"},
    ]
}


def main(request):
    return HttpResponse('Hello world!')  # вернёт страничку с надписью 'Hello world!'


def about(request):
    return HttpResponse('information page')


def get_all_news(request):
    return render(request, 'news/catalog.html', context=info)


def faq(request):
    return HttpResponse('Список вопросов и ответов')


def get_news_by_id(request, news_id):
    if news_id > 10:
        return HttpResponse('Такой новости нет', status=404)
    return HttpResponse(f'Вы открыли новость #{news_id}')  # Вернёт страницу с надписью Вы открыли новость
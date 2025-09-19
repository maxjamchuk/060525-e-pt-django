from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Article


def main(request):
    """
    Представление рендерит шаблон templates/main.html
    """

    info = {
        "users_count": 100600,
        "news_count": 10,
        "menu": [
            {"title": "Главная",
             "url": "/",
             "url_name": "index"},
            {"title": "О проекте",
             "url": "/about/",
             "url_name": "about"},
            {"title": "Каталог",
             "url": "/news/catalog/",
             "url_name": "catalog"},
        ],
    }
    return render(request, 'main.html', context=info)


def about(request):
    return HttpResponse('information page')


def catalog(request):
    return HttpResponse('Каталог новостей')


def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")


def get_all_news(request):
    articles = Article.objects.all()

    info = {
        "news": articles,
        "users_count": 100600,
        "news_count": 10,
        "menu": [
            {"title": "Главная",
             "url": "/",
             "url_name": "index"},
            {"title": "О проекте",
             "url": "/about/",
             "url_name": "about"},
            {"title": "Каталог",
             "url": "/news/catalog/",
             "url_name": "catalog"},
        ],
    }

    return render(request, 'news/catalog.html', context=info)


def faq(request):
    return HttpResponse('Список вопросов и ответов')


def get_detail_article_by_id(request, article_id):
    """
    Возвращает детальную информацию по новости для представления
    """
    article = get_object_or_404(Article, id=article_id)

    info = {
        "article": article,
        "users_count": 100600,
        "news_count": 10,
        "menu": [
            {"title": "Главная",
             "url": "/",
             "url_name": "index"},
            {"title": "О проекте",
             "url": "/about/",
             "url_name": "about"},
            {"title": "Каталог",
             "url": "/news/catalog/",
             "url_name": "catalog"},
        ],
    }

    return render(request, 'news/article_detail.html', context=info)


def get_detail_article_by_title(request, title):
    """
    Возвращает детальную информацию по новости для представления
    """
    article = get_object_or_404(Article, slug=title)
    info = {
        'article': article,
        "users_count": 5,
        "news_count": 10,
        "menu": [
            {"title": "Главная", "url": "/", "url_name": "index"},
            {"title": "О проекте", "url": "/about/", "url_name": "about"},
            {"title": "Каталог", "url": "/news/catalog/", "url_name": "catalog"},
        ],
    }
    return render(request, 'news/article_detail.html', context=info)
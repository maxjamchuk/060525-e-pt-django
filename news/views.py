from django.http import HttpResponse
from django.shortcuts import render


"""
Информация в шаблоны будет браться из базы данных
Но пока, мы сделаем переменные, куда будем записывать информацию, которая пойдет в 
контекст шаблона
"""
# Пример данных для новостей
news_dataset = [
    {
        "title": "Коты захватили правительство!",
        "content": "Вчера ночью коты совершили государственный переворот и захватили все ключевые посты в правительстве. Президент кот Мурзик обещает бесплатный вискас для всех граждан.",
        "category": "Общество",
        "tags": ["коты", "переворот", "вискас"],
        "id_author": 1,
        "id_article": 1,
        "upload_date": "2023-01-15",
        "views_count": 1000,
        "favorites_count": 500
    },
    {
        "title": "Найден новый вид единорогов!",
        "content": "Ученые обнаружили новый вид единорогов в лесах Амазонии. Эти единороги могут летать и излучают радужный свет.",
        "category": "Наука",
        "tags": ["единороги", "ученые", "наука", "открытие"],
        "id_author": 2,
        "id_article": 2,
        "upload_date": "2023-01-20",
        "views_count": 1500,
        "favorites_count": 700
    },
    {
        "title": "Земля стала квадратной!",
        "content": "Сегодня утром жители Земли проснулись и обнаружили, что наша планета стала квадратной. Ученые в шоке, но обещают разобраться в причинах.",
        "category": "Наука",
        "tags": ["земля", "квадрат", "ученые", "наука", "открытие"],
        "id_author": 1,
        "id_article": 3,
        "upload_date": "2023-02-05",
        "views_count": 2000,
        "favorites_count": 1000
    },
    {
        "title": "Собаки научились говорить!",
        "content": "Вчера собаки по всему миру начали говорить на человеческом языке. Первые слова были: 'Где моя косточка?'",
        "category": "Общество",
        "tags": ["собаки", "язык", "косточка"],
        "id_author": 2,
        "id_article": 4,
        "upload_date": "2023-02-10",
        "views_count": 1800,
        "favorites_count": 900
    },
    {
        "title": "Луна исчезла на час!",
        "content": "Вчера вечером Луна исчезла с неба на целый час. Астрономы в панике, но обещают найти объяснение.",
        "category": "Наука",
        "tags": ["луна", "исчезновение", "ученые", "наука", "открытие"],
        "id_author": 3,
        "id_article": 5,
        "upload_date": "2023-03-01",
        "views_count": 2200,
        "favorites_count": 1100
    },
    {
        "title": "Роботы захватили кухни ресторанов!",
        "content": "Роботы-повара захватили кухни всех ресторанов мира. Теперь все блюда готовятся с идеальной точностью и вкусом.",
        "category": "Технологии",
        "tags": ["роботы", "кухня", "рестораны", "переворот"],
        "id_author": 1,
        "id_article": 6,
        "upload_date": "2023-03-15",
        "views_count": 2500,
        "favorites_count": 1200
    },
    {
        "title": "Деревья начали ходить!",
        "content": "Сегодня утром деревья в парках начали ходить. Ученые предполагают, что это связано с глобальным потеплением.",
        "category": "Природа",
        "tags": ["парки", "глобальное потепление", "ученые", "наука"],
        "id_author": 2,
        "id_article": 7,
        "upload_date": "2023-04-01",
        "views_count": 2800,
        "favorites_count": 1400
    },
    {
        "title": "Вода стала розовой!",
        "content": "Вчера вода во всех реках и озерах стала розовой. Ученые обещают найти причину этого явления.",
        "category": "Природа",
        "tags": ["вода", "ученые", "наука"],
        "id_author": 3,
        "id_article": 8,
        "upload_date": "2023-04-15",
        "views_count": 3000,
        "favorites_count": 1500
    },
    {
        "title": "Люди начали летать!",
        "content": "Сегодня утром люди по всему миру начали летать. Ученые в шоке, но обещают найти объяснение этому феномену.",
        "category": "Наука",
        "tags": ["ученые", "наука", "открытие"],
        "id_author": 1,
        "id_article": 9,
        "upload_date": "2023-05-01",
        "views_count": 3200,
        "favorites_count": 1600
    },
    {
        "title": "Зомби атакуют супермаркеты!",
        "content": "Вчера ночью зомби атаковали все супермаркеты мира. Они искали свежие мозги и консервы.",
        "category": "Общество",
        "tags": ["зомби", "супермаркеты", "атака", "переворот"],
        "id_author": 2,
        "id_article": 10,
        "upload_date": "2023-05-15",
        "views_count": 3500,
        "favorites_count": 1700
    }
]

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
    "news": news_dataset  # Добавим в контекст шаблона информацию о новостях, чтобы все было в одном месте
}


def main(request):
    """
    Представление рендерит шаблон templates/main.html
    """
    return render(request, 'main.html', context=info)


def about(request):
    return HttpResponse('information page')


def catalog(request):
    return HttpResponse('Каталог новостей')


def get_category_by_name(request, slug):
    return HttpResponse(f"Категория {slug}")


def get_all_news(request):
    return render(request, 'news/catalog.html', context=info)


def faq(request):
    return HttpResponse('Список вопросов и ответов')


def get_news_by_id(request, news_id):
    if news_id > 10:
        return HttpResponse('Такой новости нет', status=404)
    return HttpResponse(f'Вы открыли новость #{news_id}')  # Вернёт страницу с надписью Вы открыли новость
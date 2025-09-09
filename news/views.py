from django.http import HttpResponse


def main(request):
    return HttpResponse('Hello world!')  # вернёт страничку с надписью 'Hello world!'


def info(request):
    return HttpResponse('information page')

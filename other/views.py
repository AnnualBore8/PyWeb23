from django.shortcuts import render

from datetime import datetime

from django.views import View
from django.http import HttpResponse

from random import random, randint
# import random

# страница 19 по 25 страницу домашняя работа в разделе Практика один, думаю, что разберусь

# random_number = random()


class CurrentDataView(View):
    """
    Выводит на сайте текущую дату и время
    """
    def get(self, request):
        html = f'{datetime.now()}'
        return HttpResponse(html)


class HelloWorld(View):
    """
    Выводит на сайте фразу 'Hello, World'
    """
    def get(self, request):
        html = 'Hello, World'
        return HttpResponse(html)


class RandomNumber(View):
    """
    Генерирует рандомное число
    """
    def get(self, request):
        random_number = randint(1, 101)
        http = f'{random_number}'
        # http = f'{random.randint(100,121)}'
        return HttpResponse(http)


class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')
from django.shortcuts import render
import random
import datetime

def index(request):
    title = 'title'
    return render(request, 'index.html', {'name': 'Psw'})


def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Psw'
    }
    context = {
        'foods': foods,
        'info': info,
    }

    return render(request, 'greeting.html', context)


def dinner(request):
    foods = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'pick': pick,
        'foods': foods,
    }
    return render(request, 'dinner.html', context)

def throw(request):
    return render(request, 'throw.html')


def catch(request):
    title = request.GET.get('title')
    context = {
        'title': title
    }
    return render(request, 'catch.html', context)


def read(request, username, article_num):
    print(username)
    print(article_num)

    context = {
        'user': username,
        'article': article_num,
    }
    return render(request, 'read.html', context)

def hws6(request):
    today = datetime.datetime.today()
    context = {
        'today': today
    }
    return render(request, 'hws6.html', context)


# Create your views here.

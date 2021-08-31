from django.urls import path
from . import views

urlpatterns = [
    path('hws6/', views.hws6, name='hws'),
    path('dinner/', views.dinner, name='dinner'),
    path('catch/', views.catch, name='catch'),
    path('throw/', views.throw, name='throw'),
    path('greeting/', views.greeting, name='greeting'),
    path('index/', views.index, name='index'),
    path('<username>/<article_num>/', views.read, name='read'),
]
from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('delete/<pk>', views.delete, name='delete'),
    path('update/<pk>/', views.update, name='update'),
    path('<pk>/edit/', views.edit, name='edit'),
    path('create/', views.create, name='create'),
    path('new/', views.new, name='new'),
    path('<pk>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]

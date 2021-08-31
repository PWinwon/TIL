from django.shortcuts import render
import datetime

def hws6(request):
    today = datetime.datetime.today()
    context = {
        'today': today
    }
    return render(request, 'hws6.html', context)


def dinner(request, menu, people):
    context = {
        'menu': menu,
        'people': people,
    }
    return render(request, 'dinner.html', context)




# Create your views here.

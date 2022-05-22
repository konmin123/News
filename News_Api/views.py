from django.shortcuts import render
from django.http import HttpResponse
from News_Mod.models import News


def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': "Список новостей"
    }
    return render(request, template_name='News_Api/index.html', context=context)

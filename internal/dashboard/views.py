from django.shortcuts import render

from dashboard.models import News

def dashboard(request):
    news = News.recent()
    return render(request, 'internal/dashboard.html', {'news_list': news,})

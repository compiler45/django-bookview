from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def splash_page(request):
    return render(request, 'splash.html')


def view_articles(request):
    return render(request, 'view_articles.html')

"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render

# 가짜 DB
movie_list = [
    {'title': '파묘', 'director': '장재현'},
    {'title': '웡카', 'director': '폴 킹'},
    {'title': '듄: 파트 2', 'director': '드니 빌뇌브'},
    {'title': '시민덕희', 'director': '박영주'},

]

def movies(request):
    return render(request, 'movies.html', {'movie_list': movie_list})


def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404

    movie = movie_list[index]
    context = {'movie': movie}
    return render(request, 'movie.html', context)


# movie 함수 같은 결과를 보여주는 다른 코드

def book_list(request):
    book_text = ''

    return render(request, 'book_list.html', {'range': range(0, 10)})


def book(request, num):

    return  render(request, template_name='book_detail.html', context={'num': num})


def gugudan(request, num):
    context = {
        'num': num,
        'results': [num * i for i in range(1, 10)]
    }
    return render(request, 'gugudan.html', context)


urlpatterns = [
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('admin/', admin.site.urls),
    path('gugu/<int:num>/', gugudan),

]

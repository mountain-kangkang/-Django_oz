"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def book_list(request):
    book_text = ''
    for i in range(0, 10):
        book_text += f'book {i}<br>'

    return HttpResponse(book_text)

movie_list = [
    {'title': '파묘', 'viewers': 11913725},
    {'title': '범죄도시4', 'viewers': 11501621},
    {'title': '인사이드 아웃 2', 'viewers': 8796146},
    {'title': '베테랑2', 'viewers': 7522494},
]

def book(request, num):
    book_text = f'book {num}번 페이지입니다.'
    return HttpResponse(book_text)

def language(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')

def python(request):
    return HttpResponse('python 페이지 입니다.')

def movies(request):
    # movie_titles = [
    #     f'<a href="/movie/{index}/">{movie['title']}</a><br>'
    #     for index, movie in enumerate(movie_list, start=1)
    # ]
    # return HttpResponse(movie_titles)
    return render(request, 'movies.html', {'movie_list' : movie_list})

def movie_detail(request, movie_id):
    if movie_id==0 or movie_id > len(movie_list):
        raise Http404
    movie = movie_list[movie_id-1]
    response_text = f'<h1>{movie["title"]}</h1> <p>관객 수 : {movie["viewers"]}</p>'
    return HttpResponse(response_text)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("book_list/", book_list, name="book_list"),
    path("book_list/<int:num>/", book, name="book"),
    path("language/python/", python),       # 얘는 language route 뒤에 호출되면 language 화면에서 <h1>태그로 호출되고 무시된다
    path("language/<str:lang>/", language, name="language"),    # 그래서 보통 str로 인자값을 넣진 않음
    path("movie/", movies, name="movies"),
    path("movie/<int:movie_id>/", movie_detail),
]

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


movie_list = [
    {'title': '파묘', 'viewers': 11913725},
    {'title': '범죄도시4', 'viewers': 11501621},
    {'title': '인사이드 아웃 2', 'viewers': 8796146},
    {'title': '베테랑2', 'viewers': 7522494},
]

books = [
    {'title': '마흔에 읽는 쇼펜하우어', 'author': '강용수'},
    {'title': '나는 메트로 폴리탄 미술관의 경비원입니다', 'author': '패트릭 브링리'},
    {'title': '불변의 법칙', 'author': '모건 하우절'},
    {'title': '세이노의 가르침', 'author': '세이노(Sayno)'},
    {'title': '모순', 'author': '양귀자'},
]

gugus = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def index(request):
    return HttpResponse("<h1>Hello, world.</h1>")

def book_list(request):
    # book_text = ''
    # for i in range(0, 10):
    #     book_text += f'book {i}<br>'
    #
    # return HttpResponse(book_text)

    return render(request,'books.html', {'books': books})

def book(request, num):
    # book_text = f'book {num}번 페이지입니다.'
    # return HttpResponse(book_text)

    if num > len(books):
        raise Http404
    return render(request, 'book.html', {'book': books[num]})

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
    return render(request, 'movie.html', {'movie' : movie})

def gugudan(request):
    return render(request, 'gugus.html', {'gugus' : gugus})

def gugu(request, num):
    return render(request, 'gugu.html', {'num' : num})

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("book_list/", book_list, name="book_list"),
    path("book_list/<int:num>/", book, name="book"),
    path("language/python/", python),       # 얘는 language route 뒤에 호출되면 language 화면에서 <h1>태그로 호출되고 무시된다
    path("language/<str:lang>/", language, name="language"),    # 그래서 보통 str로 인자값을 넣진 않음
    path("movie/", movies, name="movies"),
    path("movie/<int:movie_id>/", movie_detail),
    path("gugudan/", gugudan),
    path("gugudan/<int:num>", gugu),
]

from django.shortcuts import render
from django.http import HttpResponse

def bookmark_list(request):
    # return HttpResponse("<h1>Bookmarks List Page</h1>")
    return render(request, 'bookmark_list.html')

def bookmark_detail(request, number):
    return render(request, 'bookmark_detail.html', {'num': number})
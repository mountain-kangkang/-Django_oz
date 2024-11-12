from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from bookmark.models import Bookmark


def bookmark_list(request):
    bookmarks = Bookmark.objects.all()
    # SELECT * FROM bookmark

    context = {'bookmarks': bookmarks}
    # return HttpResponse("<h1>Bookmarks List Page</h1>")
    return render(request, 'bookmark_list.html', context)

def bookmark_detail(request, pk):
    # try:
    #     bookmark = Bookmark.objects.get(pk=pk)
    # except Bookmark.DoesNotExist:
    #     raise Http404
    bookmark = get_object_or_404(Bookmark, pk=pk)

    context = {'bookmark': bookmark}

    return render(request, 'bookmark_detail.html', context)
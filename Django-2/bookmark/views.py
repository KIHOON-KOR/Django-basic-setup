from django.http import HttpResponse,Http404
from django.shortcuts import render
from bookmark.models import Bookmark

def bookmark_list(request):
    # return HttpResponse("<h1>북마크 리스트 페이지입니다.</h1>")
    bookmarks = Bookmark.objects.filter(id__gte=5)

    context = {
        'bookmarks': bookmarks,
    }
    return render(request, 'bookmark_list.html',context)


def bookmark_detail(request, pk):
    try:
        bookmark = Bookmark.objects.get(pk=pk)
    except Bookmark.DoesNotExist:
        raise Http404

    context = {'bookmark': bookmark}
    return render(request, 'bookmark_detail.html', context)


# 같은 기능을 하는데 좀더 단순한 버전
from django.shortcuts import get_object_or_404


# def bookmark_detail(request, pk):
#     bookmark = get_object_or_404(Bookmark, pk=pk)
#
#
# context = {'bookmark': bookmark}
# return render(request, 'bookmark_detail.html', context)
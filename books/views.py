from django.shortcuts import render, get_object_or_404
from .models import Book


def index(request):
    book_list = Book.objects.order_by('-created_at')
    context = {'book_list': book_list}
    return render(request, 'index.html', context)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})

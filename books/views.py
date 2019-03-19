from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book


class IndexView(generic.ListView):
	model = Book
	ordering = ['-created_at']
	template_name = 'index.html'


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'detail.html', {'book': book})

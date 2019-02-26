from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


def index(request):
    book_list = Book.objects.order_by('-created_at')
    context = {'book_list': book_list}
    return render(request, 'index.html', context)

def detail(request, book_id):
    return HttpResponse("Hello, detail world.")

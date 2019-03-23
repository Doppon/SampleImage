from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Book


class IndexView(generic.ListView):
	model = Book
	ordering = ['-created_at']
	template_name = 'index.html'


class CreateView(generic.edit.CreateView):
	model = Book
	fields = ['title', 'logo'] 
	template_name = 'create.html'


class DetailView(generic.DeleteView):
	model = Book
	template_name = 'detail.html'


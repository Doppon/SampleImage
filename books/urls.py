from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:book_id>/', views.detail, name='detail'),
]

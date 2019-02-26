from django.db import models
from django.utils import timezone


class Book(models.Model):
  book_title = models.CharField(max_length=30)
  created_at = models.DateTimeField('登録日時', default=timezone.now)

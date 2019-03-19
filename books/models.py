from django.db import models
from django.utils import timezone
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=30)
    logo = models.ImageField('ロゴ', upload_to='images/', blank=True)
    created_at = models.DateTimeField('登録日時', default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("index")
	
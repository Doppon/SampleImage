from django.db import models
from django.utils import timezone


class Book(models.Model):
	title = models.CharField(max_length=30)
	logo = models.ImageField('ロゴ', upload_to='images/', blank=True)
	created_at = models.DateTimeField('登録日時', default=timezone.now)

	def __str__(self):
		return self.title
	
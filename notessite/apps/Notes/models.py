from django.db import models

# Create your models here.

class Note(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	added = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

from django.db import models

#our class model
class TodoItem(models.Model):
    content = models.TextField()

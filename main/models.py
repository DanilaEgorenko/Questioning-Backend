from django.db import models


class Questions(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.CharField('Автор', max_length=50)
    body = models.TextField('Анкета')

    def __str__(self):
        return self.title

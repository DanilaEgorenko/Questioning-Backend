from django.db import models
from simple_history.models import HistoricalRecords


class Questions(models.Model):
    title = models.CharField("Название", max_length=50)
    author = models.CharField("Автор", max_length=50)
    preview = models.TextField("Превью")
    body = models.TextField("Анкета")

    def __str__(self):
        return self.title

    history = HistoricalRecords()


class Review(models.Model):
    questionID = models.IntegerField()
    textReview = models.CharField("Отзыв", max_length=150)

    def __str__(self):
        return self.textReview

    history = HistoricalRecords()


class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    username = models.CharField("Никнейм", max_length=20)
    email = models.CharField("e-mail", max_length=40)

    def __str__(self):
        return self.username

    history = HistoricalRecords()


class PremiumUser(models.Model):
    id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True
    )
    level = models.PositiveIntegerField(default=1)

    history = HistoricalRecords()


class Notifications(models.Model):
    title = models.CharField("Название", max_length=20)
    receiverID = models.IntegerField()
    textNotification = models.CharField("Текст", max_length=150)

    def __str__(self):
        return self.title

    history = HistoricalRecords()


class EmailReceivers(models.Model):
    id = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True
    )
    date_subscribe = models.DateField()

    history = HistoricalRecords()

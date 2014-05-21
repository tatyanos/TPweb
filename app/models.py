from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date published')


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)


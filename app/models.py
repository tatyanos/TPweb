from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    hash = models.CharField(max_length=64)

    def __unicode__(self):
        return self.nickname


class Question(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    date = models.DateTimeField('date published')


class Answer(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date published')


class QuestionLike(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    value = models.CharField(max_length=1)


class AnswerLike(models.Model):
    user = models.ForeignKey(User)
    answer = models.ForeignKey(Answer)
    value = models.CharField(max_length=1)


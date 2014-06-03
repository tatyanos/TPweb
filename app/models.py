from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    @property
    def ans_cnt(self):
        return self.answers.count()

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question, related_name='answers')
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.text


class QuestionLike(models.Model):
    user = models.ForeignKey(User)
    value = models.SmallIntegerField()
    question = models.ForeignKey(Question)

    def __unicode__(self):
        return str(self.question) + " " + str(self.value)


class AnswerLike(models.Model):
    user = models.ForeignKey(User)
    value = models.SmallIntegerField()
    answer = models.ForeignKey(Answer)

    def __unicode__(self):
        return str(self.answer) + " " + str(self.value)


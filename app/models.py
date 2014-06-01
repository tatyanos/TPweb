from django.db import models


class User(models.Model):
    nickname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    hash = models.CharField(max_length=64)
    img = models.ImageField(upload_to='users/%Y/%m/%d')

    def __unicode__(self):
        return self.nickname


class Question(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
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


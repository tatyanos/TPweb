import os, random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asks.settings")

from app.models import User, Question, Answer, AnswerLike, QuestionLike

User.objects.all().delete()

names = ['q', 'w', 'e', 'r', 't', 'y']
for i in xrange(5):
    obj = User(nickname='user' + str(i) + random.choice(names), email='mail' + '@mail.ru', hash='test')
    obj.save()
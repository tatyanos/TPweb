import os
import random
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asks.settings")

from app.models import User, Question, Answer, AnswerLike, QuestionLike

User.objects.exclude(username='tatyana').delete()
Question.objects.all().delete()
Answer.objects.all().delete()
AnswerLike.objects.all().delete()
QuestionLike.objects.all().delete()


def get_like_value():
    return 2 * random.randint(0, 1) - 1

names = ['q', 'w', 'e', 'r', 't', 'y']
users = []
for i in xrange(10):
    obj = User(username='user' + str(i + 1),
               email='mail' + '@mail.ru',
               password='1')
    obj.save()
    users.append(obj)

questions = []
for i in xrange(25):
    obj = Question(title='Question' + str(i) + random.choice(names) + '?',
                   text='text' + random.choice(names),
                   user=random.choice(users))
    obj.save()
    questions.append(obj)

answers = []
for i in xrange(10):
    obj = Answer(text='Answer' + str(i) + random.choice(names),
                 user=random.choice(users),
                 question=random.choice(questions))
    obj.save()
    answers.append(obj)


for i in xrange(5):
    obj = AnswerLike(value=get_like_value(),
                     user=random.choice(users),
                     answer=random.choice(answers))
    obj.save()

for i in xrange(5):
    obj = QuestionLike(value=get_like_value(),
                       user=random.choice(users),
                       question=random.choice(questions))
    obj.save()

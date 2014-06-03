import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asks.settings")

from app.models import User, Question, Answer, AnswerLike, QuestionLike

USERS = 10000
QUESTIONS = 100000

users = []
for i in xrange(USERS):
    users.append(User(username='user' + str(i + 1), email='mail' + str(i + 1) + '@mail.ru', password='1'))
    if i % 1000 == 0:
        print 'u' + str(i)
User.objects.bulk_create(users)
users = None

questions = []
for i in xrange(QUESTIONS):
    questions.append(Question(title='Question' + str(i) + '?',
                              text='text' + str(i),
                              user_id=random.randint(1, USERS)))
    if i % 1000 == 0:
        print 'q' + str(i)
Question.objects.bulk_create(questions)
questions = None

for j in xrange(20):
    answers = []
    for i in xrange(QUESTIONS / 2):
        answers.append(Answer(text='Answer' + str(i),
                              user_id=random.randint(1, USERS),
                              question_id=random.randint(1, QUESTIONS)))
        if i % 1000 == 0:
            print 'a' + str(j) + '_' + str(i)
    Answer.objects.bulk_create(answers)

answers = None


# def get_like_value():
#     return 2 * random.randint(0, 1) - 1
#
# for i in xrange(5):
# obj = AnswerLike(value=get_like_value(),
#                      user=random.choice(users),
#                      answer=random.choice(answers))
#     obj.save()
#
# for i in xrange(5):
#     obj = QuestionLike(value=get_like_value(),
#                        user=random.choice(users),
#                        question=random.choice(questions))
#     obj.save()

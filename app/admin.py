from django.contrib import admin

from app.models import Question, Answer, User, QuestionLike, AnswerLike

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuestionLike)
admin.site.register(AnswerLike)
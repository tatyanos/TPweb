from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from app.models import Question


def index(request):
    #return HttpResponse("Hello, world. You're at the question index.")
    latest_question_list = Question.objects.order_by('-date')[:5]
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def like(request, question_id):
    return HttpResponse("You're liking on question %s." % question_id)
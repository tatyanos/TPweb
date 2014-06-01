from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from app.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/index.html', context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def like(request, question_id):
    return HttpResponse("You're liking on question %s." % question_id)
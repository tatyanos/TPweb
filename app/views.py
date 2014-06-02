from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from app.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/index.html', context)


def question(request, question_id):
    try:
        question_obj = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'app/detail.html', {'question': question_obj})


def add(request):
    return render(request, 'app/add.html')


def settings(request):
    return render(request, 'app/settings.html')


def register(request):
    return render(request, 'app/register.html')


def search(request):
    return render(request, 'app/search.html')


def login(request):
    return render(request, 'app/login.html')


def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)


def like(request, question_id):
    return HttpResponse("You're liking on question %s." % question_id)
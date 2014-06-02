from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse

from app.models import Question, Answer, User


def index(request):
    latest_question_list = Question.objects.order_by('-date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'app/index.html', context)


def question(request, question_id):
    question_obj = get_object_or_404(Question, pk=question_id)
    answers_list = Answer.objects.filter(question=question_obj)

    return render(request, 'app/question.html', {
        'question': question_obj,
        'answers_list': answers_list
    })


def add(request):
    return render(request, 'app/add.html')


def answer(request, question_id):
    question_obj = get_object_or_404(Question, pk=question_id)
    answer_obj = Answer(
        text=request.POST['text'],
        user=User.objects.get(username='tatyana'),
        question=question_obj)
    answer_obj.save()
    return HttpResponseRedirect(reverse('question', args=(question_id,)))


def settings(request):
    return render(request, 'app/settings.html')


def register(request):
    return render(request, 'app/register.html')


def search(request):
    return render(request, 'app/search.html')


def login(request):
    return render(request, 'app/login.html')


def like(request, question_id):
    return HttpResponse("You're liking on question %s." % question_id)
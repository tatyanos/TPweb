from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator, EmptyPage

from app.models import Question, Answer, User


@require_GET
def index_page(request, page_index, internal=False):
    page_index = int(page_index)
    if page_index == 0:
        raise Http404()
    if page_index == 1 and not internal:
        return HttpResponsePermanentRedirect(reverse('index'))

    question_list = Question.objects.order_by('-pk')
    paginator = Paginator(question_list, 10)

    try:
        page_questions = paginator.page(page_index)
    except EmptyPage:
        raise Http404()

    context = {
        'questions': page_questions,
    }
    return render(request, 'app/index.html', context)


@require_GET
def index(request):
    return index_page(request, 1, True)


@require_GET
def question(request, question_id):
    question_obj = get_object_or_404(Question, pk=question_id)
    answers_list = Answer.objects.filter(question=question_obj)

    return render(request, 'app/question.html', {
        'question': question_obj,
        'answers_list': answers_list
    })


@require_GET
@login_required
def ask(request):
    return render(request, 'app/ask.html')


@require_POST
@login_required
def ask_add(request):
    question_obj = Question(
        title=request.POST['title'],
        text=request.POST['text'],
        user=request.user)
    question_obj.save()
    return HttpResponseRedirect(reverse('question', args=(question_obj.id,)))


@require_POST
@login_required
def answer(request, question_id):
    question_obj = get_object_or_404(Question, pk=question_id)
    answer_obj = Answer(
        text=request.POST['text'],
        user=request.user,
        question=question_obj)
    answer_obj.save()
    return HttpResponseRedirect(reverse('question', args=(question_id,)))


@require_GET
@login_required
def user_settings(request):
    return render(request, 'app/user_settings.html')


@require_POST
@login_required
def user_settings_update(request):
    if request.user.email != request.POST['email']:
        request.user.email = request.POST['email']
        request.user.save()

    return HttpResponseRedirect(reverse('user_settings'))


@require_GET
def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'app/register.html')


@require_POST
def register_add(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))
    if request.POST['pswd1'] != request.POST['pswd2']:
        return HttpResponseRedirect(reverse('register'))
    User.objects.create_user(
        request.POST['username'],
        request.POST['email'],
        request.POST['pswd1'])
    return HttpResponseRedirect(reverse('django.contrib.auth.views.login'))


def search(request):
    return render(request, 'app/search.html')


def like(request, question_id):
    return HttpResponse("You're liking on question %s." % question_id)


def out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout

from app.models import Question, Answer, User

QUESTION_ON_PAGE = 10


def index_page(request, page_index, internal=False):
    page_index = int(page_index)
    if page_index == 0:
        raise Http404()
    if page_index == 1 and not internal:
        return HttpResponsePermanentRedirect(reverse('index'))
    latest_question_list = Question.objects\
        .order_by('-date')[(page_index - 1)*QUESTION_ON_PAGE:page_index*QUESTION_ON_PAGE]

    paginator = page_list(Question, page_index, QUESTION_ON_PAGE)

    context = {
        'latest_question_list': latest_question_list,
        'paginator': paginator,
        'page_current': page_index,
    }
    return render(request, 'app/index.html', context)


def index(request):
    return index_page(request, 1, True)


def page_list(classname, page_index, on_page):
    page_start = page_index - 2
    if page_start < 1:
        page_start = 1
    max_page = int(round(classname.objects.count() / on_page + 0.5))
    page_end = page_start + 5
    if page_end > max_page:
        page_end = max_page + 1
    return range(page_start, page_end)


def question(request, question_id):
    question_obj = get_object_or_404(Question, pk=question_id)
    answers_list = Answer.objects.filter(question=question_obj)

    return render(request, 'app/question.html', {
        'question': question_obj,
        'answers_list': answers_list
    })

@login_required
def ask(request):
    return render(request, 'app/ask.html')

@login_required
def ask_add(request):
    question_obj = Question(
        title=request.POST['title'],
        text=request.POST['text'],
        user=User.objects.get(username='tatyana'))
    question_obj.save()
    return HttpResponseRedirect(reverse('question', args=(question_obj.id,)))

@login_required
def answer(request, question_id):
    question_obj = get_object_or_404(Question, pk=question_id)
    answer_obj = Answer(
        text=request.POST['text'],
        user=User.objects.get(username='tatyana'),
        question=question_obj)
    answer_obj.save()
    return HttpResponseRedirect(reverse('question', args=(question_id,)))


def user_settings(request, user_id):
    return render(request, 'app/user_settings.html')


def register(request):
    return render(request, 'app/register.html')


def search(request):
    return render(request, 'app/search.html')


def like(request, question_id):
    return HttpResponse("You're liking on question %s." % question_id)


def out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
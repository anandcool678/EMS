from django.shortcuts import render
from poll.models import *
from django.http import Http404


def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html', context)


def details(request, id=None):
    context = {}
    try:
        questions = Question.objects.get(id=id)
    except:
        raise Http404
    context['questions'] = questions
    return render(request, 'polls/details.html', context)

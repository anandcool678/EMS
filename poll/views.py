from django.shortcuts import render
from poll.models import *
from django.http import Http404, HttpResponse


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



def poll(request, id=None):
    if request.method == "GET":
        try:
            questions = Question.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['questions'] = questions
        return render(request, 'polls/poll.html', context)
    if request.method == "POST":
        user_id = User.objects.get(id=1)
        data = request.POST
        ret = Answer.objects.create(user=user_id, choice_id=data['choice'])
        if ret:
            return HttpResponse("Your vote is done")
        else:
            return HttpResponse("Unseccessful vote")



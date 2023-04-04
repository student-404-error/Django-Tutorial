from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from .models import Question
# Create your views here.


def index(request):
    # loader, HttpResponse를 사용하지 않고 render를 사용하여 짧게 할 수 있음
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("You're looking at question %s" % question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
    # get_object_or_404를 이용하면 try를 사용하지 않아도 됨.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voing on question %s." % question_id)

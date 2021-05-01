from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    if request.method != 'GET':
        return HttpResponse('There has been an error processing your request.')
    latest_question = Question.objects.order_by('-pub_date')[:5]
    choices_list = Choice.objects.order_by('pk')[:5]
    context = {
        'latest_question': latest_question,
        'choices_list': choices_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    if request.method != 'GET':
        return HttpResponse('There has been an error processing your request.')
    question = Question.objects.get(pk=int(question_id))
    choices = Choice.objects.filter(question=question_id)
    print(choices)
    context = {
        'question': question,
        'choices': choices,
    }
    return render(request, 'polls/details.html', context)


def results(request, question_id):
    return HttpResponse('')


def vote(request, question_id):
    return HttpResponse('')

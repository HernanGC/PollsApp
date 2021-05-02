from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone

from inspect import currentframe

from .models import Question, Choice


def index(request):
    if request.method != 'GET':
        return render_4xx(request)
    latest_question = Question.objects.order_by('-pub_date')[:5]
    choices_list = Choice.objects.order_by('pk')[:5]
    context = {
        'latest_question': latest_question,
        'choices_list': choices_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    if request.method != 'GET':
        return render_4xx(request)
    question = Question.objects.get(pk=int(question_id))
    choices = Choice.objects.filter(question=question_id)
    context = {
        'question': question,
        'choices': choices,
    }
    return render(request, 'polls/details.html', context)


def vote(request, question_id):
    if request.method != 'POST':
        return render_4xx(request)
    try:
        choice = request.POST.__getitem__('choice') or 0
    except Exception as Exc:
        print(f'[Exception en linea~: {currentframe().f_lineno}] - [{type(Exc)}-ErrorMessage: {Exc}] - [ErrorArgs: {Exc.args}]')
        choice = 0
    if choice and int(choice) > 0:
        my_choice = Choice.objects.get(pk=int(choice))
        my_choice.vote()
        my_choice.save()
        return redirect(f'/{question_id}/results')
    return render_4xx(request, 'You must select an option')


def new_question(request):
    if request.method != 'GET':
        return render_4xx(request)
    return render(request, 'polls/new.html')


def add_question(request):
    if request.method != 'POST':
        return render_4xx(request)
    try:
        if request.POST.__getitem__('question') and request.POST.__getitem__('choice'):
            my_question = Question(question_text=request.POST.__getitem__('question'), pub_date=timezone.now())
            my_question.save()
            for choice in list(request.POST.getlist('choice')):
                new_choice = Choice(question=my_question, choice_text=choice)
                new_choice.save()
        else:
            return render_4xx(request, "You didn't type a question/choice")
    except Exception as Exc:
        print(f'[Exception en linea~: {currentframe().f_lineno}] - [{type(Exc)}-ErrorMessage: {Exc}] - [ErrorArgs: {Exc.args}]')
        return render_4xx(request)
    return redirect('index')


def results(request, question_id):
    if request.method != 'GET':
        return render_4xx(request)
    choices_result = Choice.objects.filter(question=int(question_id))
    question = Question.objects.get(pk=int(question_id))
    context = {
        'choices_result': choices_result,
        'question': question
    }
    return render(request, 'polls/results.html', context)


def render_4xx(request, answer='Sorry, there has been an error. Try again later'):
    return render(request, '4XX_error.html', {'answer': answer})

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from mysite.models import Question, Several

# Create your views here.
def defpage(request):
    return render(request, 'mysite/default_page.html')


def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'mysite/index.html', context)


def detail(request, question_num):
    question = get_object_or_404(Question, pk=question_num)
    choice_list = question.several_set.all()
    context = {'question': question, 'choice_list': choice_list}
    return render(request, 'mysite/detail.html', context)


def vote(request, question_num):
    question = get_object_or_404(Question, pk=question_num)
    try:
        selected_choice = question.several_set.get(pk=request.POST['select'])
    except(KeyError, Several.DoesNotExist):
        errmsg = "Invalid choice."
        context = {'question': question, 'error_msg': errmsg}
        return render(request, 'mysite/detai.html', context)
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('mysite:result', args=(question_num,)))


def result(request, question_num):
    question = get_object_or_404(Question, pk=question_num)
    context = {'question': question}
    return render(request, 'mysite/result.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Question, Answer, Favorite
from users.models import User
from core.forms import QuestionForm, AnswerForm


@login_required
def home(request):
    questions = Question.objects.all()
    answers = Answer.objects.all()
    return render(request, 'core/home.html', {'questions': questions,'answers': answers})


def new_question(request):
    question = Question.objects.all()
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.save()
            return redirect('home')
    else:
        form = QuestionForm()
    return render(request, 'core/new_question.html', {'form':form, 'question':question})


def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    question.delete()
    return redirect('home')

def answer_question(request, pk):
    answer = Answer.objects.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.save()
            return redirect('home')
    else:
        form = AnswerForm()
    return render(request, 'core/answer.html', {'form':form, 'answer':answer})


def favorites(request, pk):
    answer = get_object_or_404(Answer, pk=answer.pk)
    favorite = Favorite.objects.create(user=request.user, answer=answer)
    return redirect('home')
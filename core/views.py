from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from core.models import Question
from users.models import User
from core.forms import QuestionForm


# @login_required
def home(request):
    questions = Question.objects.all()
    return render(request, 'core/home.html', {'questions': questions})


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
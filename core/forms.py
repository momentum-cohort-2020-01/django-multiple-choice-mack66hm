from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from core.models import Question, Answer


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'body', 'user')


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('answer', 'body', 'user',)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from core.models import Question


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'body', 'user',)
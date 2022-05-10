from .models import Questions
from django.forms import ModelForm, TextInput


class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['title', 'author', 'body']
        widgets = {'title': TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Название анкеты'
        })}

from .models import Questions
from django.forms import ModelForm, TextInput, Textarea


class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['title', 'author', 'body']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Название анкеты'
            }),
            'author': TextInput(attrs={
                'class': 'form-user-data',
                'hidden': 'true'
            }),
            'body': Textarea(attrs={
                'class': 'form-body-data',
                'hidden': 'true'
            }),
        }

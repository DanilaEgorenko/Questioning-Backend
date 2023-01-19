from .models import Questions
from django.forms import ModelForm, TextInput, Textarea


class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ["title", "preview", "author", "body"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control form-control-lg form-control-title",
                    "placeholder": "Название анкеты",
                }
            ),
            "preview": TextInput(
                attrs={
                    "class": "form-control form-control-lg form-control-preview",
                    "placeholder": "Прикрепите URL превью в формате .jpg",
                }
            ),
            "author": TextInput(attrs={"class": "form-user-data", "hidden": "true"}),
            "body": Textarea(attrs={"class": "form-body-data", "hidden": "true"}),
        }

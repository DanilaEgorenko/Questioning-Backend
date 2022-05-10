from django.shortcuts import render, redirect
from .models import Questions
from .forms import QuestionsForm


def index(request):
    questions = Questions.objects.order_by('-id')
    return render(request, 'main/index.html', {
        'title': 'Анкетирование',
        'questions': questions
    })


def create(request):
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/create')

    form = QuestionsForm()
    context = {
        'form': form,
        'title': 'Создать анкету'
    }
    return render(request, 'main/create.html', context)


def profile(request):
    return render(request, 'main/profile.html', {
        'title': 'Мои анкеты',
    })


def login(request):
    return render(request, 'main/login.html', {
        'title': 'Вход',
    })


def question(request, id):
    question = Questions.objects.get(id=id)
    return render(request, 'main/question.html', {
        'title': 'Анкета',
        'question': question
    })

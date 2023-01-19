from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import Questions
from .forms import QuestionsForm
from django.db.models import Q
from django.core.paginator import Paginator

from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import QuestionsSerializer
from .serializers import ProfileSerializer

from rest_framework import filters


class QuestionsViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    search_fields = ["=title"]
    filter_backends = (filters.SearchFilter,)

    @action(methods=["GET"], detail=False)
    def list(self, request, page=1):
        queryset = Questions.objects.order_by("-id")
        search = ""
        if request.query_params.get("search"):
            title = request.query_params.get("search")
            search = title
            queryset = Questions.objects.filter(title__icontains=title)
        paginator = Paginator(queryset, per_page=4)
        curPage = paginator.get_page(page)

        return render(
            request,
            "main/index.html",
            {
                "title": "Анкетирование",
                "questions": paginator.get_page(page),
                "page": curPage,
                "search": search,
            },
        )


# def index(request, page=1):
#     questions = Questions.objects.order_by("-id")
#     paginator = Paginator(questions, per_page=4)
#     curPage = paginator.get_page(page)

#     return render(
#         request,
#         "main/index.html",
#         {
#             "title": "Анкетирование",
#             "questions": paginator.get_page(page),
#             "page": curPage,
#         },
#     )


def create(request):
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/create")

    form = QuestionsForm()
    context = {"form": form, "title": "Создать анкету"}
    return render(request, "main/create.html", context)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

    def list(self, request):
        search = request.GET.get("search", None)
        user = request.user.username
        if not search:
            search = ""
        queryset = Questions.objects.filter(Q(author=user) & Q(title__icontains=search))

        return render(
            request,
            "main/profile.html",
            {"title": "Мои анкеты", "questions": queryset, "search": search},
        )

    @action(methods=["POST"], detail=True)
    def delete(self, request, id):
        Questions.objects.get(Q(id=id)).delete()
        return redirect("/profile")


def question(request, id):
    question = Questions.objects.get(Q(id=id))
    return render(
        request, "main/question.html", {"title": "Анкета", "question": question}
    )


def edit(request, id):
    question = Questions.objects.get(Q(id=id))
    if request.method == "POST":
        form = QuestionsForm(request.POST, instance=question)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect("/profile")

    form = QuestionsForm()
    context = {"form": form, "question": question}
    return render(request, "main/edit.html", context)


from django.http import HttpResponseNotFound
from sentry_sdk import capture_message


def my_custom_page_not_found_view(*args, **kwargs):
    capture_message("Page not found!", level="error")
    return HttpResponseNotFound("Not found")

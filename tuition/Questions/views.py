from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth import login, logout, authenticate


class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user


class QuestionForm(forms.Form):
    question_description = forms.CharField(widget=forms.Textarea)
    question_image = forms.ImageField()


def index(request):
    if (request.method == "GET"):
        return render(request, "index.html", context={
            "form": AccountCreationForm(),
            # User should be at login view by default
            "state": "login"
        })

    elif (request.method == "POST"):
        if ("creation_form" in request.POST):
            form = AccountCreationForm(request.POST)
            if form.is_valid():
                new_account = form.save()
                return login_view(request, request.POST["username"], request.POST["password"])
            else:
                # If the form he provided is invalid, make him create again, with hints for errors
                return render(request, "index.html", context={
                    "form": form,
                    "state": "creation_form"
                })
        elif ("login_form" in request.POST):
            return login_view(request, username=request.POST['login_username'], password=request.POST['login_password'])


def login_view(request, username, password):
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "index.html", context={
            "state": "login",
            "error": "Invalid username or password!"
        })

@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def new_question(request):
    if (request.method == "GET"):
        return render(request, "new_question.html", context={
            "form": QuestionForm()
        })
    elif (request.method == "POST"):
        form = QuestionForm(request.POST, request.FILES)
        if (form.is_valid()):
            question = Question.objects.create(
                question_sender=request.user,
                question_description=form.cleaned_data.get("question_description"),
                question_image=form.cleaned_data.get("question_image")
            )
            question.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "new_question.html", context={
                "form": QuestionForm(request.POST)
            })



from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from authapp.forms import UserEditForm, UserLoginForm, UserRegisterForm

def login(request):
    title = "Login"

    login_form = UserLoginForm(data=request.POST)
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main"))

    return render(
        request,
        "authapp/login.html",
        context={
            "title": title,
            "login_form": login_form,
        },
    )


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def register(request):
    title = "Register"

    if request.method == "POST":
        register_form = UserRegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = UserRegisterForm()

    return render(
        request,
        "authapp/register.html",
        context={
            "title": title,
            "register_form": register_form,
        },
    )


def edit(request):
    title = "Editing"

    if request.method == "POST":
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = UserEditForm(instance=request.user)

    return render(
        request,
        "authapp/edit.html",
        context={
            "title": title,
            "edit_form": edit_form,
        },
    )

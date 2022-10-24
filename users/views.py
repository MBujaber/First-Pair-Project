from django.shortcuts import render, redirect
from .forms import UserRegister, UserLogin, UpdateUserForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)

            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)



def logout_user(request):
    logout(request)
    return redirect("home")



def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)

            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)

    context = {
        "form": user_form,
    }
    return render(request, "edit_profile.html", context)
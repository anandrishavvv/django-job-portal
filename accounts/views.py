from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegisterForm, CandidateProfileForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("job_list")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request, user)

            return redirect("job_list")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def upload_resume(request):

    profile = getattr(request.user, "candidateprofile", None)

    if request.method == "POST":

        form = CandidateProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

    if form.is_valid():

     profile = form.save(commit=False)

    profile.user = request.user

    # Delete old resume if uploading a new one
    if request.user.candidateprofile:
        old_profile = request.user.candidateprofile

        if (
            old_profile.resume
            and "resume" in request.FILES
            and old_profile.resume != profile.resume
        ):
            old_profile.resume.delete(save=False)

    profile.save()

    return redirect("job_list")
 
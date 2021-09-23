from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile
from .forms import ProfileModelForm, SKillModelForm


def index(request):
    profiles = Profile.objects.all()
    return render(request, "developers/profiles.html", {"profiles": profiles})


@login_required
def single_profile(request, username):
    try:
        profile = Profile.objects.get(user__username__iexact=username)
    except ObjectDoesNotExist:
        return HttpResponse("Profile Not Created Yet")
    context = {
        "profile": profile,
    }
    if profile.user == request.user:
        return render(
            request=request, template_name="developers/account.html", context=context
        )
    return render(
        request=request, template_name="developers/profile.html", context=context
    )


@login_required
def edit_profile(request):
    profile = request.user.profile
    form = ProfileModelForm(instance=profile, initial={"username": profile.user.username})
    if request.method != "POST":
        return render(
            request=request,
            template_name="developers/profile_form.html",
            context={"form": form},
        )

    form = ProfileModelForm(
        data=request.POST,
        instance=profile,
        files=request.FILES,
    )
    if form.is_valid():
        profile = form.save(commit=False)
        username = form.cleaned_data["username"]
        profile.user.username = username
        profile.user.save()
        form.save()
    return redirect("developers:profile", username=profile.user.username)


@login_required
def add_skill(request, username):
    user = User.objects.get(username__iexact=username)
    if user != request.user:
        return redirect('developers:profile', username=username)

    form = SKillModelForm()

    if request.method == "POST":
        form = SKillModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            profile = request.user.profile
            skill = form.instance
            profile.skills.add(skill)
            return redirect("developers:profile", username=profile.user.username)

    return render(request=request, template_name="developers/add_skill.html", context={"form": form})
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from apps.core.constants.messages import (
    SkillAddedSuccessfully,
    SkillDeletedSuccessfully,
    SkillUpdatedSuccessfully,
)

from .forms import ProfileModelForm, SKillModelForm
from .models import Profile, Skill


def index(request):
    profiles = Profile.objects.all()
    qs = []
    query = request.GET.get("text")
    if not query:
        return render(
            request,
            template_name="developers/profiles.html",
            context={"profiles": profiles},
        )

    profiles = Profile.objects.filter(
        Q(user__username__icontains=query)
        | Q(user__first_name__icontains=query)
        | Q(user__last_name__icontains=query)
        | Q(short_intro__icontains=query)
        | Q(location__icontains=query)
        | Q(boi__icontains=query)
        | Q(skills__title__icontains=query)
        | Q(skills__description__icontains=query)
    ).order_by("user__username", "user__first_name", "user__last_name").distinct()

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
    form = ProfileModelForm(
        instance=profile, initial={"username": profile.user.username}
    )
    if request.method != "POST":
        return render(
            request=request,
            template_name="developers/profile_form.html",
            context={"form": form},
        )

    form = ProfileModelForm(data=request.POST, instance=profile, files=request.FILES,)
    if form.is_valid():
        profile = form.save(commit=False)
        username = form.cleaned_data["username"]
        profile.user.username = username
        profile.user.save()
        form.save()
    return redirect("developers:profile", username=profile.user.username)


@login_required
def add_skill(request, username):
    user = get_object_or_404(User, username__iexact=username)
    if user != request.user:
        return redirect("developers:profile", username=username)

    form = SKillModelForm()
    skills = Skill.objects.filter(title__iexact=request.POST.get("title"))
    if request.method == "POST":
        form = SKillModelForm(request.POST or None)
        if form.is_valid():
            profile = request.user.profile
            if skills.exists():
                skill = skills.first()
            else:
                skill = form.instance
                form.save()
            profile.skills.add(skill)
            messages.success(request, SkillAddedSuccessfully.text)
            return redirect("developers:profile", username=profile.user.username)

    return render(
        request=request,
        template_name="developers/add_skill.html",
        context={"form": form},
    )


@login_required
def edit_skill(request, username, slug):
    user = get_object_or_404(User, username__iexact=username)
    if user != request.user:
        return redirect("developers:profile", username=username)
    skill = get_object_or_404(Skill, slug=slug)
    form = SKillModelForm(instance=skill)

    if request.method == "POST":
        form = SKillModelForm(data=request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, SkillUpdatedSuccessfully.text)
            return redirect("developers:profile", username=request.user.username)

    return render(
        request=request,
        template_name="developers/add_skill.html",
        context={"form": form, "skill": skill},
    )


def delete_skill(request, username, slug):
    user = get_object_or_404(User, username__iexact=username)
    if user != request.user:
        return redirect("developers:profile", username=username)
    skill = get_object_or_404(Skill, slug=slug)
    if request.method == "POST":
        profile = user.profile
        profile.skills.remove(skill)
        messages.success(request, SkillDeletedSuccessfully.text)
        return redirect("developers:profile", username=request.user.username)

    return render(
        request=request,
        template_name="developers/delete.html",
        context={
            "skill": skill,
            "back": f"/developers/{request.user.username}/",
            "action": f"/developers/{request.user.username}/delete_skill/{slug}/",
        },
    )

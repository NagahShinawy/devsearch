from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.projects.models import Project
from .forms import ProjectModelForm


def projects(request):
    projs = Project.objects.all()
    return render(
        request, template_name="projects/projects.html", context={"projects": projs}
    )


def project(request, uuid):
    try:

        single = Project.objects.get(uuid__iexact=uuid)
    except ObjectDoesNotExist:
        return HttpResponse("Not Found")
    tags = single.tags.all()
    return render(
        request,
        template_name="projects/single-project.html",
        context={"project": single, "tags": tags},
    )


def create_project(request):
    project_form = ProjectModelForm()
    if request.method == "POST":
        project_form = ProjectModelForm(request.POST)
        if project_form.is_valid():
            project_form.save()
            return redirect("projects:projects")
        else:
            print("errors")
    return render(request, template_name="projects/form-template.html", context={"form": project_form})

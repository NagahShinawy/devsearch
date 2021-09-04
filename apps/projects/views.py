from django.shortcuts import render, redirect

from apps.projects.models import Project
from .forms import ProjectModelForm
from apps.core import utils


def projects(request):
    projs = Project.objects.all()
    return render(
        request, template_name="projects/projects.html", context={"projects": projs}
    )


def single_project(request, uuid):
    project = utils.get_object_or_404(model=Project, uuid=uuid)
    tags = project.tags.all()
    return render(
        request,
        template_name="projects/single-project.html",
        context={"project": project, "tags": tags},
    )


def create_project(request):
    project_form = ProjectModelForm()
    if request.method == "POST":
        project_form = ProjectModelForm(data=request.POST)
        if project_form.is_valid():
            project_form.save()
            return redirect("projects:projects")
    return render(
        request,
        template_name="projects/form-template.html",
        context={"form": project_form},
    )


def delete_project(request, uuid):
    project = utils.get_object_or_404(model=Project, uuid=uuid)
    if request.method == "POST":
        project.delete()
        return redirect("projects:projects")
    return render(request, template_name="projects/delete.html", context={"project": project})

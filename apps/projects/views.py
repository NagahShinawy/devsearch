from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
    if project is False:
        return HttpResponse("Not Found")
    tags = project.tags.all()
    return render(
        request,
        template_name="projects/single-project.html",
        context={"project": project, "tags": tags},
    )


@login_required
def create_project(request):
    project_form = ProjectModelForm()
    if request.method == "POST":
        project_form = ProjectModelForm(data=request.POST, files=request.FILES)
        if project_form.is_valid():
            project_form.save()
            return redirect("projects:projects")
    return render(
        request,
        template_name="projects/form-template.html",
        context={"form": project_form},
    )


@login_required
def delete_project(request, uuid):
    project = utils.get_object_or_404(model=Project, uuid=uuid)

    if project is False:
        return HttpResponse("Not Found")

    if request.method == "POST":
        project.delete()
        return redirect("projects:projects")
    return render(
        request, template_name="projects/delete.html", context={"project": project}
    )


@login_required
def update_project(request, uuid):
    project = utils.get_object_or_404(model=Project, uuid=uuid)

    if project is False:
        return HttpResponse("Not Found")

    form = ProjectModelForm(instance=project)
    if request.method == "POST":
        form = ProjectModelForm(
            data=request.POST, instance=project, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect("projects:projects")
    return render(
        request,
        template_name="projects/form-template.html",
        context={"project": project, "form": form},
    )

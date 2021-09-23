from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.core import utils
from apps.projects.models import Project

from .forms import ProjectModelForm


def list_projects(request):
    projects = Project.objects.all()
    return render(
        request, template_name="projects/projects.html", context={"projects": projects}
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
            project = project_form.instance
            project.owner = request.user.profile
            project.save()
            project_form.save()
            return redirect("developers:profile", username=request.user.username)
    return render(
        request,
        template_name="projects/form-template.html",
        context={"form": project_form},
    )


@login_required
def delete_project(request, uuid):
    # project = utils.get_object_or_404(model=Project, uuid=uuid)
    project = request.user.profile.projects.get(uuid=uuid)

    if project.owner.user != request.user:
        return redirect("developers:index")

    if project is False:
        return HttpResponse("Not Found")

    if request.method == "POST" and project.owner.user == request.user:
        project.delete()
        return redirect("developers:profile", username=request.user.username)
    return render(
        request, template_name="projects/delete.html", context={"project": project}
    )


@login_required
def update_project(request, uuid):
    # project = utils.get_object_or_404(model=Project, uuid=uuid)
    project = request.user.profile.projects.get(uuid=uuid)
    if project.owner.user != request.user:
        return redirect("developers:index")

    if project is False:
        return HttpResponse("Not Found")

    form = ProjectModelForm(instance=project)
    if request.method == "POST" and project.owner.user == request.user:
        form = ProjectModelForm(
            data=request.POST, instance=project, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect("developers:profile", username=request.user.username)
    return render(
        request,
        template_name="projects/form-template.html",
        context={"project": project, "form": form},
    )

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from apps.projects.models import Project


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

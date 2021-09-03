from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from apps.projects.models import Project

sehhaty = {
    "id": 1,
    "name": "Sehhaty",
    "users": 45345,
    "developers": 20,
}

gcc = {
    "id": 2,
    "name": "gcc",
    "users": 900,
    "developers": 80,
}

anat = {
    "id": 3,
    "name": "Anat",
    "users": 1010,
    "developers": 120,
}

apps = [sehhaty, gcc, anat]


def projects(request):
    projs = Project.objects.all()
    return render(request, template_name="projects/projects.html", context={"projects": projs})


def project(request, uuid):
    try:

        single = Project.objects.get(uuid__iexact=uuid)
    except ObjectDoesNotExist:
        return HttpResponse("Not Found")
    return render(
        request,
        template_name="projects/single-project.html",
        context={"project": single},
    )

from django.shortcuts import render


def projects(request):
    return render(request, template_name="projects/projects.html")


def project(request, uuid):
    return render(request, template_name="projects/single-project.html")


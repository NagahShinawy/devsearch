from django.shortcuts import render


def projects(request):
    return render(request, template_name="projects/projects.html")


def project(request, uuid):
    sehhaty = {
        "name": "Sehhaty",
        "users": 45345,
        "developers": 20,
    }

    gcc = {
        "name": "gcc",
        "users": 900,
        "developers": 80,
    }
    apps = [sehhaty, gcc]

    return render(
        request,
        template_name="projects/single-project.html",
        context={"apps": apps, "sehhaty": sehhaty, "gcc": gcc},
    )

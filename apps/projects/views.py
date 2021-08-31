from django.shortcuts import render

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
    return render(request, template_name="projects/projects.html")


def project(request, uuid):
    single_app = None
    for app in apps:
        if app["id"] == uuid:
            single_app = app
            break

    return render(
        request,
        template_name="projects/single-project.html",
        context={"apps": apps, "sehhaty": sehhaty, "gcc": gcc, "app": single_app},
    )

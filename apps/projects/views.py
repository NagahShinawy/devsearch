from django.http import HttpResponse


def projects(request):
    return HttpResponse("These are Projects")
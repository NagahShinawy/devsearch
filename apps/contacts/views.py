from django.shortcuts import render


def inbox(request):
    return render(request, template_name="contacts/inbox.html")

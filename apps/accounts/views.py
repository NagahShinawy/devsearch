from django.shortcuts import render


def profile(request):
    return render(request=request, template_name="accounts/profile.html")
from django import forms
from .models import Profile


class ProfileModelForm(forms.ModelForm):
    username = forms.CharField(max_length=256)

    class Meta:
        model = Profile
        exclude = ("user", )
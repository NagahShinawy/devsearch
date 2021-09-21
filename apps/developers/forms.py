from django.forms import models
from .models import Profile


class ProfileModelForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "__all__"
        )
        exclude = ("user", )
        labels = {"first_name": "Your First Name"}
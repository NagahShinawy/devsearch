from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .styles import fields_style


class ProfileCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )
        labels = {"first_name": "Your First Name"}

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)

        for field in fields_style:
            field_name = field["field_name"]
            attrs = field["attrs"]
            self.fields[field_name].widget.attrs.update(**attrs)

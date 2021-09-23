from django import forms
from .models import Profile, Skill


class ProfileModelForm(forms.ModelForm):
    username = forms.CharField(max_length=256)

    class Meta:
        model = Profile
        fields = (
            "username",
            "image",
            "facebook",
            "twitter",
            "github",
            "linkedin",
            "stackoverflow",
            "youtube",
            "website",
            "short_intro",
            "location",
            "boi",
            "skills",
        )

        exclude = ("user",)
        widgets = {"skills": forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super(ProfileModelForm, self).__init__(*args, **kwargs)
        # self.fields["title"].widget.attrs.update({"class": "input input--text", "placeholder": "Enter Title"})
        for name, _ in self.fields.items():
            self.fields[name].widget.attrs.update({"class": "input"})


class SKillModelForm(forms.ModelForm):

    class Meta:
        model = Skill
        fields = ("title", "description")

    def __init__(self, *args, **kwargs):
        super(SKillModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs.update({"class": "input"})
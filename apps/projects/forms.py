from django import forms
from .models import Project


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("title", "tags", "description", "source_link", "demo_link", "image")
        widgets = {"tags": forms.CheckboxSelectMultiple}

    def __init__(self, *args, **kwargs):
        super(ProjectModelForm, self).__init__(*args, **kwargs)
        # self.fields["title"].widget.attrs.update({"class": "input input--text", "placeholder": "Enter Title"})
        for name, field in self.fields.items():
            self.fields[name].widget.attrs.update({"class": "input"})

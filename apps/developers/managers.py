from django.db import models


class SkillManager(models.Manager):

    @property
    def base_skills(self):
        return self.exclude(description__iexact="")

    @property
    def other_skills(self):
        return self.filter(description__iexact="")
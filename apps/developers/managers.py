from django.db import models


class SkillManager(models.Manager):

    @property
    def base(self):
        return self.exclude(description__iexact="")

    @property
    def others(self):
        return self.filter(description__iexact="")
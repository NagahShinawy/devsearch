from django.db import models
from django.db.models import Q


class SkillManager(models.Manager):
    @property
    def base(self):
        return self.exclude(description__iexact="")

    @property
    def others(self):
        return self.filter(description__iexact="")


class DeveloperManager(models.Manager):
    def get_by_name(self, value):
        return self.filter(
            Q(user__username__icontains=value)
            | Q(user__first_name__icontains=value)
            | Q(user__last_name__icontains=value)
        )

    def get_by_short_intro(self, value):
        return self.filter(short_intro__icontains=value)

    def get_by_location(self, value):
        return self.filter(location__icontains=value)

    def get_by_boi(self, value):
        return self.filter(boi__icontains=value)

    def get_by_skill(self, value):
        return self.filter(
            Q(skills__title__icontains=value) | Q(skills__description__icontains=value)
        )

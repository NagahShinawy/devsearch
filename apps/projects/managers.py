from django.db import models
from django.db.models import Q


class ProjectManager(models.Manager):
    def get_by_title(self, title):
        return self.filter(title__icontains=title)

    def get_by_description(self, description):
        return self.filter(description__icontains=description)

    def get_by_developer(self, dev):
        return self.filter(
            Q(owner__user__username__icontains=dev)
            | Q(owner__user__first_name__icontains=dev)
            | Q(owner__user__last_name__icontains=dev)
            | Q(owner__user__email__icontains=dev)
        )

    def get_by_tag(self, tag):
        return self.filter(tags__name__icontains=tag)

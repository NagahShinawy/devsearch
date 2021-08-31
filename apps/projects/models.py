from django.db import models
from apps.core.db.models import UUIDMixin, InfoMixin, SlugMixin, TimestampMixin


class Project(UUIDMixin, InfoMixin, SlugMixin, TimestampMixin):

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "Project"
        verbose_name_plural = "Lean Projects"


class Task(models.Model):
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

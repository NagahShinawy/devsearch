import uuid
from django.db import models
from apps.core.db.models import UUIDMixin, InfoMixin, SlugMixin, TimestampMixin
from .choices import VoteType


class Project(UUIDMixin, InfoMixin, SlugMixin, TimestampMixin):
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "Project"
        verbose_name_plural = "Lean Projects"


class Review(UUIDMixin, TimestampMixin, models.Model):
    # owner

    # on_delete ==> what you will do with children if parent deleted ?
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=256, choices=VoteType.choices)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.value


class Tag(UUIDMixin, TimestampMixin, models.Model):
    name = models.CharField(max_length=256)
    projects = models.ManyToManyField(Project, related_name="tags")

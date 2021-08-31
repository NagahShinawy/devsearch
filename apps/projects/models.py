from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.db.models import UUIDMixin, InfoMixin, SlugMixin, TimestampMixin
from .choices import VoteType


class Project(UUIDMixin, InfoMixin, SlugMixin, TimestampMixin):
    source_link = models.URLField(null=True, blank=True, verbose_name=_("Source Link"))
    demo_link = models.URLField(null=True, blank=True, verbose_name=_("Demo Link"))
    votes = models.IntegerField(default=0, verbose_name=_("Votes"))
    vote_ratio = models.IntegerField(default=0, verbose_name=_("Votes Ratio"))
    tags = models.ManyToManyField(
        "projects.Tag", null=True, blank=True, verbose_name=_("Tags")
    )  # 'app_label.ModelName'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "Project"
        verbose_name_plural = "Lean Projects"


class Review(UUIDMixin, TimestampMixin, models.Model):
    # owner

    # on_delete ==> what you will do with children if parent deleted ?
    body = models.TextField(null=True, blank=True, verbose_name=_("Body"))
    value = models.CharField(
        max_length=256, choices=VoteType.choices, verbose_name=_("Value"), default=VoteType.UP
    )

    proj = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Project"),
    )

    def __str__(self):
        return self.value

    def project(self):
        return self.proj

    def content(self):
        if self.body:
            return self.body[:30]
        return "-"


class Tag(UUIDMixin, TimestampMixin, models.Model):
    name = models.CharField(max_length=256, verbose_name=_("Name"))

    def __str__(self):
        return self.name

from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.core.db.models import UUIDMixin, InfoMixin, SlugMixin, TimestampMixin, ImageModelMixin
from .choices import VoteType
from apps.core import utils


class Project(UUIDMixin, InfoMixin, SlugMixin, TimestampMixin, ImageModelMixin):
    POSITIVE = "Positive"
    NEGATIVE = "Negative"

    source_link = models.URLField(null=True, blank=True, verbose_name=_("Source Link"))
    demo_link = models.URLField(null=True, blank=True, verbose_name=_("Demo Link"))
    votes = models.IntegerField(default=0, verbose_name=_("Votes"))
    vote_ratio = models.IntegerField(default=0, verbose_name=_("Votes Ratio"))
    tags = models.ManyToManyField(
        "projects.Tag",
        null=True,
        blank=True,
        verbose_name=_("Tags"),
        related_name="projects",
    )  # 'app_label.ModelName'

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
        verbose_name = "Project"
        verbose_name_plural = "Lean Projects"

    def tags_list(self):
        return utils.from_qs_to_list(self.tags.all())

    @property
    def feedback(self):
        if self.vote_ratio >= 50:
            return self.POSITIVE
        return self.NEGATIVE


class Review(UUIDMixin, TimestampMixin, models.Model):
    # owner

    proj = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Project"),
    )
    # on_delete ==> what you will do with children if parent deleted ?
    body = models.TextField(null=True, blank=True, verbose_name=_("Body"))
    value = models.CharField(
        max_length=256,
        choices=VoteType.choices,
        verbose_name=_("Value"),
        default=VoteType.UP,
    )

    def __str__(self):
        return self.body[:30]

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

    def projects_list(self):
        return utils.from_qs_to_list(self.projects.all())

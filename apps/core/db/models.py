import datetime
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


def model_directory(instance, filename):
    return (
        f"{instance.__class__.__name__.lower()}/"
        f"{datetime.date.today().year}/"
        f"{datetime.date.today().month}/{filename}"
    )


class UUIDMixin(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=False
    )


class TimestampMixin(models.Model):
    created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Created at"), null=True, blank=True
    )
    updated = models.DateTimeField(
        auto_now=True, verbose_name=_("Updated at"), null=True, blank=True
    )  # last save

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(null=True, blank=True, verbose_name=_("Slug"))

    class Meta:
        abstract = True


class InfoMixin(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.TextField(
        max_length=225, null=True, blank=True, verbose_name=_("Description")
    )

    class Meta:
        abstract = True


class ImageModelMixin(models.Model):
    image = models.ImageField(
        upload_to=model_directory, blank=True, null=True, verbose_name=_("image")
    )

    class Meta:
        abstract = True

    @property
    def image_url(self):
        try:
            return self.image.url
        except (TypeError, ValueError, AttributeError):
            return str()

    @property
    def image_name(self):
        try:
            return self.image.name.split("/")[-1]
        except (TypeError, ValueError, AttributeError, IndexError):
            return str()


class SocialMediaLinksMixin(models.Model):
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    class Meta:
        abstract = True

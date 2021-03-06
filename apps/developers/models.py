from django.contrib.auth.models import User
from django.db import models

from apps.core.db.models import (
    ImageModelMixin,
    InfoMixin,
    SlugMixin,
    SocialMediaLinksMixin,
    TimestampMixin,
    UUIDMixin,
)

from .managers import SkillManager


class Skill(InfoMixin, SlugMixin, TimestampMixin, models.Model):

    objects = SkillManager()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.title


class Profile(
    UUIDMixin, ImageModelMixin, SocialMediaLinksMixin, TimestampMixin, models.Model
):
    IMAGE_URL = "/static/images/profile-pics/user-default.png"

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile", null=True, blank=True
    )
    short_intro = models.CharField(max_length=256, null=True, blank=True)
    location = models.CharField(max_length=256, null=True, blank=True)
    boi = models.TextField(max_length=256, null=True, blank=True)
    skills = models.ManyToManyField(
        Skill, related_name="profile", null=True, blank=True
    )

    def __str__(self):
        return self.user.username

    def social_links(self):
        links = {
            "github": self.github,
            "stackoverflow": self.stackoverflow,
            "twitter": self.twitter,
            "linkedin": self.linkedin,
            "facebook": self.facebook,
            "globe": self.website,
        }
        return {website: url for website, url in links.items() if url}

    def base_skills(self):
        return self.skills.base

    def other_skills(self):
        return self.skills.others

    class Meta:
        ordering = ["-created"]

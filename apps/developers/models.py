from django.db import models
from django.contrib.auth.models import User
from .managers import SkillManager
from apps.core.db.models import (
    UUIDMixin,
    ImageModelMixin,
    SocialMediaLinksMixin,
    TimestampMixin,
    InfoMixin,
)


class Skill(InfoMixin, TimestampMixin, models.Model):

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
    skills = models.ManyToManyField(Skill, related_name="profile")

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

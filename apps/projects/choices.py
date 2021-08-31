from django.db import models


class VoteType(models.TextChoices):
    UP = ("up", "Up Vote")
    DOWN = ("down", "Down Vote")

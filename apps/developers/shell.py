from django.utils.text import slugify


from .models import Skill


def update_skills_slugs():
    for skill in Skill.objects.all():
        skill.slug = slugify(skill.title)
        skill.save()

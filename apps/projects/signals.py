import logging
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Project

logger = logging.getLogger(__name__)


def get_project_representation(instance):
    project = f"{instance.uuid}-{instance.title}" if instance.uuid else instance.title
    return project


@receiver(pre_save, sender=Project, dispatch_uid="update_slug_unlisted")
def update_slug(sender, instance, **kwargs):
    project = get_project_representation(instance)
    if instance.slug is None:
        instance.slug = slugify(instance.title)
        logger.info(f"Update 'slug' for <'{sender.__class__}'> <{project}> to <{instance.slug}>")
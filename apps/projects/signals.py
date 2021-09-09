import logging
import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify
from .models import Project

logger = logging.getLogger(__name__)


def get_project_representation(instance):
    project = f"{instance.uuid}-{instance.title}" if instance.uuid else instance.title
    return project


@receiver(pre_save, sender=Project, dispatch_uid="update_slug")
def update_slug(sender, instance, **kwargs):
    project = get_project_representation(instance)
    if instance.slug is not None:
        return
    instance.slug = slugify(instance.title)
    logger.info(f"Update 'slug' for {sender} <{project}> to <{instance.slug}>")


@receiver(post_delete, sender=Project, dispatch_uid="delete_img")
def delete_img(sender, instance, **kwargs):
    project = get_project_representation(instance)
    if not instance.image:
        return
    os.remove(instance.image.path)
    logger.info(f"image <{instance.image}>  for {sender} <{project}> was deleted")
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


def from_qs_to_list(qs: models.QuerySet) -> list:
    return [obj for obj in qs]


def get_object_or_404(model, uuid):
    try:
        obj = model.objects.get(uuid__iexact=uuid)
        return obj
    except ObjectDoesNotExist:
        return False

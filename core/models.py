from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class BaseModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name=_("criado em"), blank=True, null=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name=_("atualizado em"), blank=True, null=True
    )

    class DoesNotExists(Exception):
        pass

    class Meta:
        abstract = True

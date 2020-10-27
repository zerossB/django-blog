import hashlib
import urllib
import uuid

from core.models import BaseModel
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from tinymce.models import HTMLField


# Create your models here.
class User(AbstractUser, BaseModel):

    uuid = models.UUIDField(_("uuid"), editable=False, default=uuid.uuid4)
    excerpt = HTMLField(default="", null=True, blank=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = "users"

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users_detail", kwargs={"pk": self.pk})

    def get_gravatar_url(self, size=150):
        default = (
            "https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y"
        )
        return "https://www.gravatar.com/avatar/%s?%s" % (
            hashlib.md5(self.email.lower().encode("utf-8")).hexdigest(),
            urllib.parse.urlencode({"d": default, "s": str(size)}),
        )


class Social(models.Model):

    user = models.OneToOneField(
        "users.User",
        verbose_name=_("User"),
        on_delete=models.CASCADE,
        null=True,
        default=True,
    )

    linkedin = models.CharField(_("Linkedin Social"), max_length=200)
    twitter = models.CharField(_("Twitter Social"), max_length=200)
    facebook = models.CharField(_("Facebook Social"), max_length=200)

    class Meta:
        db_table = "social"
        verbose_name = "Social"
        verbose_name_plural = "Socials"

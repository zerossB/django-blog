from core.models import BaseModel
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from tinymce.models import HTMLField


# Create your models here.
class Post(BaseModel):

    title = models.CharField(_("Post Title"), max_length=255)
    slug = models.SlugField(_("Post Slug"), unique=True)
    excerpt = models.TextField(_("Post Excerpt"))
    content = HTMLField()
    author = models.ForeignKey(
        "users.User",
        verbose_name=_("Post Author"),
        on_delete=models.CASCADE,
        related_name="author_posts",
    )
    tags = models.ManyToManyField(
        "posts.Tag",
        verbose_name=_("Post Tags"),
        related_name="tag_posts",
        blank=True,
    )
    image = models.FileField(
        _("Post Image"), upload_to="posts/", max_length=250, default="", blank=True
    )
    is_active = models.BooleanField(_("Post Active"), default=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        db_table = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})


class Tag(models.Model):
    name = models.CharField(_("Tag Name"), max_length=50)
    slug = models.SlugField(_("Tag Slug"))
    excerpt = models.TextField(_("Tag Excerpt"), null=True, blank=True)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        db_table = "tags"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags:detail", kwargs={"pk": self.pk})

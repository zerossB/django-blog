from django.contrib import admin

from .forms import PostForm, TagForm
from .models import Post, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    add_form = PostForm
    form = PostForm
    list_display = ("title", "author", "is_active", "updated_at", "created_at")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    add_form = TagForm
    form = TagForm
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}

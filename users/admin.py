from django.contrib import admin

from .forms import UserChangeForm, UserCreationForm
from .models import Social, User


class SocialsInlines(admin.TabularInline):
    model = Social


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ("email", "name", "is_active")
    inlines = [SocialsInlines]

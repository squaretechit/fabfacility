from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin

from .models import Gallery


admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    list_display = (
        'first_name',
        'last_name',
        'username',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'last_login'
        )
    list_display_links = ('username',)


@admin.register(Gallery)
class CustomGallery(admin.ModelAdmin):
    list_display = (
        'date',
        'project_name',
        'project_location'
    )
    list_display_links = ('project_name',)
    list_filter = (
        'date',
        'project_name',
        'project_location'
    )
    search_fields=(
        'project_name',
        'project_location'
    )

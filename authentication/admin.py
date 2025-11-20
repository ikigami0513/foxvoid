from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html

from unfold.admin import ModelAdmin
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.decorators import display
from modeltranslation.admin import TranslationAdmin
from typing import Optional
from .models import User, GroupProxy


admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin, TranslationAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = [
        "username",
        "email",
        "display_header_country",
        "is_staff"
    ]

    fieldsets = [
        [
            None, 
            {
                "fields": [
                    "username", 
                    "password"
                ]
            }
        ],
        [
            _("Personal info"),
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "email",
                    "country",
                    "timezone",
                    "avatar"
                ]
            }
        ],
        [
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions"
                ]
            }
        ],
        [
            _("Important dates"),
            {
                "fields": [
                    "last_login",
                    "date_joined"
                ]
            }
        ]
    ]

    search_fields = ["username", "first_name", "last_name", "email"]
    list_filter = [
        "is_staff",
        "is_superuser",
        "is_active",
        "groups",
        "country"
    ]

    @display(
        description=_("Country")
    )
    def display_header_country(self, obj: User) -> Optional[str]:
        if not obj.country:
            return None
        
        return format_html(
            '<div style="display: flex; align-items: center;">'
            '<img src="{}" style="width: 20px; height: auto; margin-right: 8px;" alt="{}"/>'
            '<span>{}</span>'
            '</div>',
            obj.country.flag,
            obj.country.name,
            obj.country.name
        )
    

@admin.register(GroupProxy)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

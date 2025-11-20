import uuid, os
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.translation import gettext as _
from django_countries.fields import CountryField
from timezone_field import TimeZoneField
from .managers import UserManager


def user_avatar_file_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return os.path.join(f"users/avatars/{instance.id}.{uuid.uuid4()}{file_extension}")


class User(AbstractUser):
    objects = UserManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    avatar = models.ImageField(verbose_name=_("avatar"), upload_to=user_avatar_file_path, null=True, blank=True)
    country = CountryField(blank=True, null=True, blank_label='(Select country)')
    timezone = TimeZoneField(default='UTC')

    def get_initials(self) -> str:
        """
        Returns the first two characters of the username in uppercase.
        If username is empty, returns "?".
        Example: "foxvoid" -> "FO"
        """
        if not self.username:
            return "?"
        return self.username[:2].upper()


class GroupProxy(Group):
    class Meta:
        proxy = True
        app_label = 'authentication'
        verbose_name = Group._meta.verbose_name
        verbose_name_plural = Group._meta.verbose_name_plural

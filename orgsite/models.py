from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static


def logo_upload_path(instance, filename):
    return './storage/org_{}_{}'.format(instance.user.username, filename)

class Organization(models.Model):
    name = models.CharField(name='Org_Name', max_length=150)
    category = models.CharField(max_length=50)
    user = models.OneToOneField(User, related_name='organization')
    shortcut = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    description = models.TextField()
    logo = models.ImageField(upload_to=logo_upload_path, blank=True)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('img/UP_logo.png')

    def __str__(self):
        return self.Org_Name

    
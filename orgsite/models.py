from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Organization(models.Model):
    name = models.CharField(name='Org_Name', max_length=150)
    category = models.CharField(max_length=50)
    user = models.ForeignKey(User, unique=True)
    shortcut = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    description = models.TextField()
    image = models.ImageField(upload_to='org_logo', blank=True)

    def __str__(self):
        return self.Org_Name

    
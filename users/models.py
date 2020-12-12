# django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

from django.contrib.auth.models import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    fb_token = models.CharField(max_length=300)
    fb_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = 'Facebook User'
        verbose_name_plural = 'Facebook Users'

    # def __str__(self):
    #     return f'{self.fb_id}'

    # def save(self, *args, **kwargs):
    #     user = super().save(*args, **kwargs)
    #     user.set_password('Pwd@12345')
    #     return user
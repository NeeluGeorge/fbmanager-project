# django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    fb_id = models.CharField(max_length=100)
    fb_token = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    password = None
    USERNAME_FIELD = 'fb_id'
    REQUIRED_FIELDS = ['fb_id', 'token']

    class Meta:
        verbose_name = 'Facebook User'
        verbose_name_plural = 'Facebook Users'

    def __str__(self):
        return f'{self.name}_{self.fb_id}'

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    passport_img = models.FileField(null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    is_phone_confirmed = models.BooleanField(default=False)
    is_passport_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email


from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    city = models.CharField(max_length=64, verbose_name="Город", blank=True)
    phone_number = models.CharField(max_length=14, verbose_name="Телефон", blank=True)

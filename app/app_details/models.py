from django.conf import settings
from django.db import models


# Create your models here.
class AppDetails(models.Model):
    app_name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    framework = models.CharField(max_length=20)
    plan_type = models.CharField(max_length=20)
    database_type = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)


class EnvironmentDetails(models.Model):
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=50)
    app_name = models.ForeignKey(AppDetails, on_delete=models.CASCADE, related_name='env_vars')


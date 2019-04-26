from django.db import models
from djutil.models import TimeStampedModel


class User(TimeStampedModel):
    github_username = models.CharField(max_length=100)

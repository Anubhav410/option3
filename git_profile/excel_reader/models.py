from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.

class FileData(TimeStampedModel):
    name = models.CharField(max_length=100)
    data = models.TextField(help_text="Storing Excel sheet data in json dump format")
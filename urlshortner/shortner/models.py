from django.db import models
import uuid

# Create your models here.

class Url(models.Model):
    link = models.CharField(max_length=1000)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    clicks = models.IntegerField(default=0)
    
    def __str__(self):
        return self.link

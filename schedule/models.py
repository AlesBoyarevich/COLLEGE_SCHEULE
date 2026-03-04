from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='media/teachers')
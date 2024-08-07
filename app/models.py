from django.db import models

# Create your models here.

class Tod(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)


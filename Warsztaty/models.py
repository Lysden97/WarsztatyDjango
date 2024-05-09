from django.db import models

# Create your models here.

class Sale(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

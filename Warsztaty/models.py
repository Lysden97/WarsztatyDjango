from django.db import models

# Create your models here.

class Sale(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    projector_availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Rezerwacja(models.Model):
    sale_id = models.ForeignKey(Sale, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('sale_id', 'date')
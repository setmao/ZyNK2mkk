from django.db import models

# Create your models here.
class Coffee(models.Model):
    class Meta:
        verbose_name = "Coffee"
        verbose_name_plural = "Coffees"

    def __str__(self):
        pass
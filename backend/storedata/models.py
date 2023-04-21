from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

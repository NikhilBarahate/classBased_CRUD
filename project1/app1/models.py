from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=100)
    marks = models.FloatField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

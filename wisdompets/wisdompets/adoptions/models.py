from django.db import models


# Create your models here.
class Pet(models.Model):
    SEX_CHOICES = [('M', 'MALE'), ('F', 'FEMALE')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

    def __str__(self):
        return self.name


class Vaccine(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

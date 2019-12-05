from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class Resort(models.Model):
    resort_name = models.CharField(max_length=200)
    resort = models.IntegerField(primary_key=True)
    beginner = models.FloatField()
    intermediate = models.FloatField()
    expert = models.FloatField()
    def __str__(self):
        return self.resort_name
    def get_absolute_url(self):
        return reverse('resort-detail',args=[str(self.resort)])

class Choice(models.Model):
    user = models.CharField(max_length=200)
    input_beginner = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    input_intermediate = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    input_expert = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    def __str__(self):
        return self.user
    def get_absolute_url(self):
        return reverse('resort-detail', args=[str(self.id)])


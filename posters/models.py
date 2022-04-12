from django.db import models
from django.contrib.auth.models import User


class Motive(models.Model):
    """ The model for motives / Categories """

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        """ Defines the model name in plural """
        verbose_name_plural = 'Motives'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ Returns the friendly name of a motive """
        return self.friendly_name


class Poster(models.Model):
    """ The model for the Poster product """
    name = models.CharField(max_length=200)
    motive = models.ForeignKey(
        'Motive', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    size = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    like = models.ManyToManyField(
        User, related_name='poster_like', blank=True)

    def __str__(self):
        return self.name

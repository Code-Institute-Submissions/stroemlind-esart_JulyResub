from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class Customer(models.Model):
    """
    A model for maintaining default delivery information and
    order history for registered customers
    """
    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    defualt_email = models.EmailField(
        max_length=200,
        null=True,
        blank=True
    )
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_postcode = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    default_town_or_city = models.CharField(
        max_length=85,
        null=True,
        blank=True
    )
    default_country = CountryField(
        blank_label='(Select Country)',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.customer.username


@receiver(post_save, sender=User)
def create_or_update_customer_info(sender, instance, created, **kwargs):
    """
    A function to create or update the user profile
    """
    if created:
        Customer.objects.create(customer=instance)

    instance.customer.save()

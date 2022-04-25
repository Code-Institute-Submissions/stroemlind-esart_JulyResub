import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from posters.models import Poster


class Order(models.Model):
    """
    The model handling Orders
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=85, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    total_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        Code from Boutique Ado
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        Codebase from Boutique Ado
        """
        self.order_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.total_cost = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        Code from Boutique Ado
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model for each line of the order
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    poster = models.ForeignKey(
        Poster,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.poster.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Name {self.poster.name} on order {self.order.order_number}'

from django.db import models


class NewsletterSubscriber(models.Model):
    """
    A model to collect email for Newsletter
    subcriptions
    """
    news_email = models.EmailField()
    subscribe_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class RequestPoster(models.Model):
    """
    The model to take request for customized Posters
    """
    full_name = models.CharField(max_length=70, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    motive = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name

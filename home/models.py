from django.db import models


class NewsletterSubscriber(models.Model):
    """
    A model to collect email for Newsletter 
    subcriptions
    """
    email = models.EmailField()
    subscribe_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

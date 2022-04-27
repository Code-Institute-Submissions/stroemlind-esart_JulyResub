from django.contrib import admin
from .models import NewsletterSubscriber


class NewsletterAdmin(admin.ModelAdmin):
    """
    Admin model to handle newsletter subscribers
    from the admin panel
    """
    list_display = ('email', 'subscribe_date')

    ordering = ('subscribe_date',)


admin.site.register(NewsletterSubscriber, NewsletterAdmin)

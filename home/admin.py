from django.contrib import admin
from .models import NewsletterSubscriber, RequestPoster


class NewsletterAdmin(admin.ModelAdmin):
    """
    Admin model to handle newsletter subscribers
    from the admin panel
    """
    list_display = ('news_email', 'subscribe_date')

    ordering = ('subscribe_date',)


class RequestPosterAdmin(admin.ModelAdmin):
    """
    Admin model to handel customized poster requests
    """
    list_display = (
        'full_name',
        'email',
        'phone_number',
        'date',
        'motive',
        'image',
    )

    ordering = ('date',)


admin.site.register(NewsletterSubscriber, NewsletterAdmin)
admin.site.register(RequestPoster, RequestPosterAdmin)

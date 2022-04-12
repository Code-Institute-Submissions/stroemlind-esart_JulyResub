from django.contrib import admin
from .models import Motive, Poster


class PosterAdmin(admin.ModelAdmin):
    """ An admin class for Poster products """
    list_display = (
        'name',
        'motive',
        'description',
        'price',
        'image',
    )

    ordering = ('name',)


class MotiveAdmin(admin.ModelAdmin):
    """ An admin class for Motive/Categories """
    list_display = (
        'name',
        'friendly_name',
    )


admin.site.register(Poster, PosterAdmin)
admin.site.register(Motive, MotiveAdmin)

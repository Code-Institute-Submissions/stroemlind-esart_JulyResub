# Generated by Django 3.2 on 2022-04-29 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_requestposter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newslettersubscriber',
            old_name='email',
            new_name='news_email',
        ),
    ]
# Generated by Django 2.0.6 on 2018-06-22 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Snipet',
            new_name='Snippet',
        ),
    ]

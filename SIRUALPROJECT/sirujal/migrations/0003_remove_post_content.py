# Generated by Django 3.0.4 on 2020-05-21 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirujal', '0002_post_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]

# Generated by Django 3.0.4 on 2020-05-28 06:10

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sirujal', '0004_auto_20200527_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]

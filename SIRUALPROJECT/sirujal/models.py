from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = RichTextUploadingField(blank=True, null=True)
   

class Video(models.Model):
    title = models.CharField(null=True, max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description2 = RichTextUploadingField(blank=True, null=True, config_name='special', 
    external_plugin_resources=[('youtube', '/static/admin/css/vendor/ckeditor_plugin/youtube/youtube/youtube/', 'plugin.js',
    )],
    )


    def save(self):
        super(Blog, self).save()

    def save(self):
        super(Video, self).save()
        


    def __str__(self):
        return '%s' % self.title
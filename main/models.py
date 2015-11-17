from django.db import models

# Create your models here.


class Tweets(models.Model):
    created_at = models.CharField(max_length=100, null=True, blank=True)
    screen_name = models.CharField(max_length=100, null=True, blank=True)
    profile_image_url = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    # text = models.ForeignKey(text, null=True, blank=True)
    text = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.screen_name

# profile_image_url, screen_name, created_at, time)zone, location

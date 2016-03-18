from django.db import models

# Create your models here.

class Video(models.Model):
    title = models.sCharField(max_lenght=200)
    video_link = models.CharField(max_length=200)

    def __str__(self):
        return self.video_link
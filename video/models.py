from django.db import models
import json

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200, default='a title')
    video_link = models.CharField(max_length=200)

    def __str__(self):
        return self.video_link

class Note(models.Model):
    note_title = models.CharField(max_length=200, default='a title')
    word_list = models.CharField(max_length=500)
    sentence_list = models.CharField(max_length=500)
    video = models.ForeignKey(Video)
   # order = models.IntegerField(default=0)

    #class Meta:
        #ordering = ['order',]

    def set_word_list(self, x):
        self.word_list = json.dumps(x)

    def get_word_list(self, x):
        return json.loads(self.word_list)

    def __str__(self):
        return self.note_title



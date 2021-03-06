import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Sentence(models.Model):
    sentence_text = models.CharField(max_length=2000, default="")
    chinese_text = models.CharField(max_length=2000, default="")
    pub_date = models.DateTimeField('date published', default="")
    user = models.ForeignKey(User, default="")

    def __str__(self):
    	return self.sentence_text

    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

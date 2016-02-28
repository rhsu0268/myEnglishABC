from django.db import models

# Create your models here.

class Sentence(models.Model):
    sentence_text = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')


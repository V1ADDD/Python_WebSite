from django.db import models

class Ask(models.Model):
    date = models.CharField('date', max_length=10)
    time = models.CharField('time', max_length=5)
    gmail = models.CharField('gmail', max_length=50)
    question = models.TextField('question')

    def __str__(self):
        return self.gmail

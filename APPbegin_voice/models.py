from django.db import models

class audio_book(models.Model):
    num = models.CharField(max_length=22)
    book = models.CharField(max_length=255)
    amoChars = models.CharField(max_length=25)

    def __str__(self):
        a = str(self.book) + '---' + str(self.amoChars)
        return a 

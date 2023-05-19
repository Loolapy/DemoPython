from django.db import models

# Create your models here.

class movie(models.Model):
    name=models.CharField(max_length=200)
    dec=models.TextField()
    Year=models.IntegerField()
    img=models.ImageField(upload_to='Photos')

    def __str__(self):
        return self.name


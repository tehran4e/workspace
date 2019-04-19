from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    story = models.TextField()
    artistsName = models.ManyToManyField(Artist, blank=True)


from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100, blank=False)
    year = models.IntegerField()
    director = models.CharField(max_length=50, blank=True)
    photo = models.FileField(blank= True)
    
    def __str__(self):
        return self.title

GENRE_CHOICES = (('C', 'Classic'), ('H', 'Happy'), ('S', 'Sad'), ('D', 'Devotional'), ('M', 'Melody'),)

class Audio(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    genre = models.CharField(max_length=1, choices = GENRE_CHOICES)
    songs = models.FileField(blank = True)
    
    def __str__(self):
        return self.title

class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    genre = models.CharField(max_length=1, choices = GENRE_CHOICES)
    songs = models.FileField(blank = True)
    
    def __str__(self):
        return self.title
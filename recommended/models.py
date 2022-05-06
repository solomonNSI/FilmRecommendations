from django.db import models

class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=200)

    class Meta:
        ordering = ['movie_genre']

    def __str__(self):
        return self.movie_name

class Recommendation(models.Model):
    movies = models.ManyToManyField(Movie)
    result = models.TextField()

    def __str__(self):
        return self.result

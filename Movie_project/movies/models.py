from django.db import models

# Create your models here.
class Movie(models.Model):
    poster = models.ImageField(blank=True,upload_to='posters/')
    background = models.ImageField(blank=True,upload_to='posters/')
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    director = models.CharField(max_length=100)
    actors = models.TextField()
    release_date = models.DateField()
    
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review of {self.movie.title} by {self.reviewer_name}'

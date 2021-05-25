from django.db import models
from django.db.models.deletion import CASCADE



class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    

    class Meta:
        db_table = 'movies'


class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    movie = models.ManyToManyField(Movie, db_table="actors_movies")

    class Meta:
        db_table = 'actors'

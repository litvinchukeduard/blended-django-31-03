from django.db import models

# Create your models here.
# Cinema (name, location, capacity)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

# Movie (title (str), director (str), description (str), duration (int), release_date)
class Movie(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    duration = models.PositiveIntegerField()
    release_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title}, director: {self.director}'
    

# Screening (start_time (DateTi­meField), end_time (DateTi­meField))
class Screening(models.Model):
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Starting at {self.start_time}, ending at {self.end_time}'

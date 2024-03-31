from django.db import models

# Create your models here.
# Cinema (name, location, capacity)


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    

# Movie (title (str), director (str), description (str), duration (int))
    
# Screening (start_time (DateTi­meField), end_time (DateTi­meField))
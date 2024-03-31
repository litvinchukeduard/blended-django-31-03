from django.contrib import admin

from .models import Cinema, Movie, Screening

# Register your models here.
admin.site.register(Cinema)
admin.site.register(Movie)
admin.site.register(Screening)

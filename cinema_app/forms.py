from django import forms

from .models import Cinema, Movie, Screening

class CinemaForm(forms.ModelForm):
    class Meta:
        model = Cinema
        # fields = ['name', 'location', 'capacity']
        fields = '__all__'
        

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # fields = ['name', 'location', 'capacity']
        fields = '__all__'


class ScreeningForm(forms.ModelForm):
    class Meta:
        model = Screening
        # fields = ['name', 'location', 'capacity']
        fields = '__all__'
        
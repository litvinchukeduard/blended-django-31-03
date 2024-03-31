from django.shortcuts import render, redirect

from .forms import CinemaForm, MovieForm, ScreeningForm

from .models import Cinema, Movie, Screening

# Create your views here.
def main(request):
    cinemas = Cinema.objects.all()
    movies = Movie.objects.all()
    screenings = Screening.objects.all()
    return render(request, 'cinema_app/index.html', {
        'cinemas': cinemas,
        'movies': movies,
        'screenings': screenings
    })

def cinema(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_app:index')
        else:
            return render(request, 'cinema_app/cinema.html', {'form': form})
    return render(request, 'cinema_app/cinema.html', {'form': CinemaForm()})

def movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_app:index')
        else:
            return render(request, 'cinema_app/movie.html', {'form': form})
    return render(request, 'cinema_app/movie.html', {'form': MovieForm()})

def screening(request):
    if request.method == 'POST':
        form = ScreeningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_app:index')
        else:
            return render(request, 'cinema_app/screening.html', {'form': form})
    return render(request, 'cinema_app/screening.html', {'form': ScreeningForm()})

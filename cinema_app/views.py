from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CinemaForm, MovieForm, ScreeningForm

from .models import Cinema, Movie, Screening

# Create your views here.
def main(request):
    page_number = request.GET.get('page', 1)

    cinemas = Cinema.objects.all().order_by('id')
    movies = Movie.objects.all()
    screenings = Screening.objects.all()

    paginator = Paginator(list(movies), 2)
    movies_page = paginator.page(page_number)

    return render(request, 'cinema_app/index.html', {
        'cinemas': cinemas,
        'movies': movies_page,
        'screenings': screenings
    })

@login_required
def cinema(request):
    if request.method == 'POST':
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_app:index')
        else:
            return render(request, 'cinema_app/cinema.html', {'form': form})
    return render(request, 'cinema_app/cinema.html', {'form': CinemaForm()})

@login_required
def movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_app:index')
        else:
            return render(request, 'cinema_app/movie.html', {'form': form})
    return render(request, 'cinema_app/movie.html', {'form': MovieForm()})

@login_required
def screening(request):
    if request.method == 'POST':
        form = ScreeningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cinema_app:index')
        else:
            return render(request, 'cinema_app/screening.html', {'form': form})
    return render(request, 'cinema_app/screening.html', {'form': ScreeningForm()})

from django.shortcuts import render, redirect

from .forms import CinemaForm, MovieForm, ScreeningForm

# Create your views here.
def main(request):
    return render(request, 'cinema_app/index.html')

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

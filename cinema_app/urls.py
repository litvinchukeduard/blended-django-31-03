from django.urls import path

from . import views

app_name = 'cinema_app'

urlpatterns = [
    path('', views.main, name='index'),
    path('cinema/', views.cinema, name='cinema'),
    path('movie/', views.movie, name='movie'),
    path('screening/', views.screening, name='screening'),
]

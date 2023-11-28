
from django.contrib import admin
from django.urls import path
from AppCoder.views import (show_html, mostrar_peliculas, crear_peliculas_form, busqueda_peli
, crear_pelicula, crear_series_form,mostrar_series,busqueda_serie,busqueda_Tvshow,crear_Tvshows_form,mostrar_Tvshows)

urlpatterns = [
    path('crear_pelicula/', crear_pelicula),
    path('show/', show_html),
    path('peliculas/', mostrar_peliculas),
    path('pelicula/', crear_peliculas_form),
    path('encontrar/', busqueda_peli),
    path('serie/', crear_series_form),
    path('series/', mostrar_series),
    path('encontrarSerie/', busqueda_serie),
    path('Tvshow/', crear_Tvshows_form),
    path('Tvshows/', mostrar_Tvshows),
    path('encontrarTvshow/', busqueda_Tvshow),




]

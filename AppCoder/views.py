from django.shortcuts import render,redirect
from AppCoder.models import Pelicula, Serie, Tvshow
from AppCoder.forms import PeliculaForm, busquedaPeliculaForm, SerieForm,busquedaSerieForm,TvshowForm,busquedaTvshowForm
from django.http import HttpResponse


def crear_pelicula(request):
    pelicula = Pelicula(nombre='titanic', anio= 1997)
    pelicula.save()
    contexto = {"pelicula":pelicula}

    return redirect("/app/peliculas/")


def show_html(request):
    contexto={}
    return render(request, 'base.html', contexto)

def mostrar_peliculas(request):
    peliculas = Pelicula.objects.all()
    contexto ={
        "peliculas": peliculas,
        "form":  busquedaPeliculaForm()
    }
    return render(request,"AppCoder/peliculas.html", contexto)

def crear_peliculas_form(request):
    if request.method == "POST":
        pelicula_formulario = PeliculaForm(request.POST)
        if pelicula_formulario.is_valid():
            informacion = pelicula_formulario.cleaned_data
            pelicula_crear = Pelicula(nombre=informacion["nombre"], anio=informacion["anio"])
            pelicula_crear.save()
            return redirect("/app/peliculas/")

    pelicula_formulario = PeliculaForm()
    contexto = {
        "form": pelicula_formulario
    }
    return render(request, "AppCoder/crear_pelicula.html", contexto)

def busqueda_peli(request):
    nombre = request.GET["nombre"]
    peliculas= Pelicula.objects.filter(nombre__icontains=nombre)

    contexto = {
        "peliculas": peliculas,
        "form": busquedaPeliculaForm(),
    }
    return render(request, "AppCoder/peliculas.html", contexto)

def crear_series_form(request):
    if request.method == "POST":
        serie_formulario = SerieForm(request.POST)
        if serie_formulario.is_valid():
            informacion = serie_formulario.cleaned_data
            serie_crear = Serie(nombre=informacion["nombre"], cantidad_de_capitulos=informacion["cantidad_de_capitulos"])
            serie_crear.save()
            return redirect("/app/series/")

    serie_formulario = SerieForm()
    contexto = {
        "form": serie_formulario
    }
    return render(request, "AppCoder/crear_serie.html", contexto)

def mostrar_series(request):
    series = Serie.objects.all()
    contexto ={
        "series": series,
        "form":  busquedaSerieForm(),
    }
    return render(request,"AppCoder/series.html", contexto)


def busqueda_serie(request):
    nombre = request.GET["nombre"]
    series = Serie.objects.filter(nombre__icontains=nombre)

    contexto = {
        "series": series,
        "form": busquedaSerieForm(),
    }
    return render(request, "AppCoder/series.html", contexto)

def crear_Tvshows_form(request):
    if request.method == "POST":
        tvshow_formulario = TvshowForm(request.POST)
        if tvshow_formulario.is_valid():
            informacion = tvshow_formulario.cleaned_data
            tvshow_crear = Tvshow(nombre=informacion["nombre"], pais_de_origen=informacion["pais_de_origen"])
            tvshow_crear.save()
            return redirect("/app/Tvshows/")

    tvshow_formulario = TvshowForm()
    contexto = {
        "form": tvshow_formulario
    }
    return render(request, "AppCoder/crear_Tvshow.html", contexto)

def mostrar_Tvshows(request):
    Tvshows = Tvshow.objects.all()
    contexto ={
        "Tvshows": Tvshows,
        "form":  busquedaTvshowForm(),

    }
    return render(request,"AppCoder/Tvshows.html", contexto)


def busqueda_Tvshow(request):
    nombre = request.GET["nombre"]
    Tvshows = Tvshow.objects.filter(nombre__icontains=nombre)

    contexto = {
        "Tvshows": Tvshows,
        "form": busquedaTvshowForm(),
    }
    return render(request, "AppCoder/Tvshows.html", contexto)

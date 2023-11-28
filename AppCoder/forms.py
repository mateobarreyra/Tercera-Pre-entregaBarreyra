from django import forms

class PeliculaForm(forms.Form):
    nombre = forms.CharField()
    anio =forms.IntegerField()

class busquedaPeliculaForm(forms.Form):
    nombre= forms.CharField()

class SerieForm(forms.Form):
    nombre = forms.CharField()
    cantidad_de_capitulos =forms.IntegerField()

class busquedaSerieForm(forms.Form):
    nombre= forms.CharField()

class TvshowForm(forms.Form):
    nombre = forms.CharField()
    pais_de_origen= forms.CharField()

class busquedaTvshowForm(forms.Form):
    nombre= forms.CharField()
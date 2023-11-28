from django.db import models

class Pelicula(models.Model):
    nombre=models.CharField(max_length=40)
    anio=models.IntegerField(max_length=20)

    def __str__(self):
        return f"Pelicula: {self.nombre}, Anio: {self.anio}"

class Serie(models.Model):
    nombre = models.CharField(max_length=40)
    cantidad_de_capitulos = models.IntegerField(max_length=20)

    def __str__(self):
        return f"Pelicula: {self.nombre}, Cantidad de capitulos: {self.cantidad_de_capitulos}"

class Tvshow(models.Model):
    nombre = models.CharField(max_length=40)
    pais_de_origen = models.CharField(max_length=20)

    def __str__(self):
        return f"Pelicula: {self.nombre}, Pais de origen: {self.pais_de_origen}"



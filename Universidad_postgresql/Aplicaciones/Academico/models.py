from django.db import models
from django.utils.html import format_html


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=31)
    creditos = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} ({})'.format(self.nombre, self.creditos)

    def coloreado(self):
        if self.creditos >= 4:
            style = '<span style="color: blue;">{0}</span>'.format(self.nombre)
        else:
            style = '<span style="color: red;">{0}</span>'.format(self.nombre)
        return format_html(style)

    coloreado.short_description = 'Cursos'

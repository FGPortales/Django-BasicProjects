from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    servicio = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    ip_cliente = models.CharField(max_length=255)
    user = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    puerto = models.CharField(max_length=255)
    sector = models.CharField(max_length=255)
    ci = models.CharField(max_length=255)

    def __str__(self):
        return f'Cliente {self.id}: {self.nombre}'


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre}'


class Marca(models.Model):
    nombre = models.CharField(max_length=255)
    categoria_id = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, blank=True, null=True, db_column='categoria_id')

    def __str__(self):
        return f'{self.nombre} - {self.categoria_id}'


class Acceso(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre}'


class Contacto(models.Model):
    nom_contacto = models.CharField(max_length=255)
    tel_contacto = models.CharField(max_length=255)
    correo_contacto = models.CharField(max_length=255)


class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    version = models.CharField(max_length=255, default='')
    marca_id = models.ForeignKey(
        Marca, on_delete=models.CASCADE, default=False, db_column='marca_id', verbose_name='Marca')
    licencia_equipo = models.DateField()
    acceso_lan = models.CharField(max_length=255, default='')
    acceso_wan = models.CharField(max_length=255, default='')
    user = models.CharField(max_length=255, default='')
    password = models.CharField(max_length=255, default='')
    serie = models.CharField(max_length=255, default='')
    puerto_ssh = models.CharField(max_length=255, default='')
    acceso_id = models.ForeignKey(
        Acceso, on_delete=models.CASCADE, blank=True, null=True, db_column='acceso_id', verbose_name='Acceso')



from django.contrib import admin
from profiles_api import models

# Register your models here.
admin.site.register(models.UserProfile)  # le damos acceso al administrador para que pueda editar los modelos

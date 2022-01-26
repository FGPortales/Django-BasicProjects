from django.forms import ModelForm, EmailInput

from clientes.models import Cliente, Marca, Categoria, Acceso, Equipo


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }


class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {}


class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {}


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {}


class AccesoForm(ModelForm):
    class Meta:
        model = Acceso
        fields = '__all__'
        widgets = {}

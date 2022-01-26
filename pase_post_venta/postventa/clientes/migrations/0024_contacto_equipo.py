# Generated by Django 3.2.9 on 2021-12-07 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0023_acceso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_contacto', models.CharField(max_length=255)),
                ('tel_contacto', models.CharField(max_length=255)),
                ('correo_contacto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('modelo', models.CharField(max_length=255)),
                ('version', models.CharField(default='', max_length=255)),
                ('licencia_equipo', models.CharField(default='', max_length=255)),
                ('acceso_lan', models.CharField(default='', max_length=255)),
                ('acceso_wan', models.CharField(default='', max_length=255)),
                ('user', models.CharField(default='', max_length=255)),
                ('password', models.CharField(default='', max_length=255)),
                ('serie', models.CharField(default='', max_length=255)),
                ('marca_id', models.ForeignKey(db_column='marca_id', default=False, on_delete=django.db.models.deletion.CASCADE, to='clientes.marca')),
            ],
        ),
    ]
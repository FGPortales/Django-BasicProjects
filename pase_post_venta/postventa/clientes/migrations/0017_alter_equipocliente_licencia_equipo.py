# Generated by Django 3.2.9 on 2021-12-07 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_equipocliente_licencia_equipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipocliente',
            name='licencia_equipo',
            field=models.CharField(default='', max_length=255),
        ),
    ]

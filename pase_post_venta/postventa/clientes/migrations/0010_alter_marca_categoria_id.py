# Generated by Django 3.2.9 on 2021-12-07 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0009_marca_categoria_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='categoria_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.categoria'),
        ),
    ]

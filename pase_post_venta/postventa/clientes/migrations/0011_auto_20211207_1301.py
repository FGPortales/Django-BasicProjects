# Generated by Django 3.2.9 on 2021-12-07 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0010_alter_marca_categoria_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipocliente',
            name='marcar_id',
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='marca_id',
            field=models.ForeignKey(db_column='marca_id', default=False, on_delete=django.db.models.deletion.CASCADE, to='clientes.marca'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='categoria_id',
            field=models.ForeignKey(blank=True, db_column='categoria_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.categoria'),
        ),
    ]

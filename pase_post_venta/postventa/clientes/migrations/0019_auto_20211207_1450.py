# Generated by Django 3.2.9 on 2021-12-07 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0018_auto_20211207_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='acceso_lan',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='acceso_wan',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='licencia_equipo',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='password',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='serie',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='user',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='equipocliente',
            name='acceso_id',
            field=models.ForeignKey(blank=True, db_column='acceso_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.acceso'),
        ),
    ]

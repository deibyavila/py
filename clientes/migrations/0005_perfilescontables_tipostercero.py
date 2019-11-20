# Generated by Django 2.2.6 on 2019-11-18 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20191117_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilesContables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TiposTercero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 2.2.6 on 2019-11-17 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tercero',
            name='foto',
            field=models.ImageField(blank=True, upload_to='static/tercero'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-27 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motores', '0001_initial'),
        ('motos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='m',
            name='motor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='motores.motor'),
        ),
    ]

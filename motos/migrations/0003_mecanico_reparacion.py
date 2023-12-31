# Generated by Django 4.2.5 on 2023-09-29 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motos', '0002_m_motor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripccion', models.CharField(max_length=50)),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motos.mecanico')),
            ],
        ),
    ]

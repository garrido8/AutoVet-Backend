# Generated by Django 5.0.3 on 2025-06-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('en_proceso', 'En proceso'), ('resuelta', 'Resuelta'), ('esperando', 'Esperando cliente')], default='pendiente', max_length=20),
        ),
    ]

# Generated by Django 5.0.3 on 2025-06-06 15:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointment', '0001_initial'),
        ('staff', '0002_staff_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentShare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(choices=[('readonly', 'Read-Only'), ('editing', 'Editing')], default='readonly', max_length=20)),
                ('shared_at', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shares', to='appointment.appoinment')),
                ('shared_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='staff.staff')),
                ('shared_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_appointments', to='staff.staff')),
            ],
            options={
                'unique_together': {('appointment', 'shared_with')},
            },
        ),
    ]

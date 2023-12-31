# Generated by Django 5.0 on 2023-12-17 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('starting_time', models.DateField()),
                ('ending_time', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('codeforces_handle', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('P', 'Present'), ('A', 'Absent'), ('E', 'Excused')], default='A', max_length=25)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance_event', to='base.event')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='attendee', to='base.student')),
            ],
        ),
    ]

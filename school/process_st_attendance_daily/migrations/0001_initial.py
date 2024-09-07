# Generated by Django 5.1.1 on 2024-09-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_date', models.DateField()),
                ('shift', models.CharField(max_length=50)),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('duration', models.DurationField()),
                ('attendance_type', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late'), ('Half-day', 'Half-day')], max_length=20)),
                ('late_by_min', models.IntegerField(blank=True, null=True)),
                ('early_gone_by_min', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

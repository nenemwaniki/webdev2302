# Generated by Django 5.0.2 on 2024-03-08 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=10, unique=True)),
                ('course_name', models.CharField(max_length=100)),
                ('course_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SpecialEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_description', models.TextField()),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_venue', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_code', models.CharField(max_length=10, unique=True)),
                ('unit_name', models.CharField(max_length=100)),
                ('unit_description', models.TextField()),
                ('unit_lecturer', models.CharField(max_length=100)),
                ('unit_semester', models.IntegerField()),
                ('unit_venue', models.CharField(max_length=100)),
                ('unit_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_reg', models.CharField(max_length=10, unique=True)),
                ('student_name', models.CharField(max_length=100)),
                ('student_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schedule.courses')),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.students')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.units')),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='course_units',
            field=models.ManyToManyField(related_name='courses', to='schedule.units'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-03-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='units',
            field=models.ManyToManyField(blank=True, related_name='courses', to='schedule.units'),
        ),
    ]

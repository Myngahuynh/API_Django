# Generated by Django 4.2.11 on 2024-03-05 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='care_name',
            new_name='car_name',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-26 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sham', '0005_alter_profile_date_created_lekh'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lekh',
            old_name='user',
            new_name='profile',
        ),
    ]
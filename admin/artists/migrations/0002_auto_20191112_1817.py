# Generated by Django 2.2.7 on 2019-11-12 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artists',
            old_name='moods_des',
            new_name='artists_des',
        ),
        migrations.RenameField(
            model_name='artists',
            old_name='moods_name',
            new_name='artists_name',
        ),
    ]

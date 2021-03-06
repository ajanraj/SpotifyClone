# Generated by Django 2.2.7 on 2019-11-13 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('moods', '0001_initial'),
        ('genre', '0001_initial'),
        ('artists', '0002_auto_20191112_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=100)),
                ('song_des', models.CharField(default='This is a Popular Song!', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('song_length', models.CharField(max_length=10)),
                ('song_file', models.FileField(upload_to='songs/')),
                ('artists', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Artists')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genre.Genre')),
                ('moods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moods.Moods')),
            ],
        ),
    ]

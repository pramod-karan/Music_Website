# Generated by Django 3.0.6 on 2020-05-30 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('director', models.CharField(blank=True, max_length=50)),
                ('photo', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('C', 'Classic'), ('H', 'Happy'), ('S', 'Sad'), ('D', 'Devotional'), ('M', 'Melody')], max_length=1)),
                ('songs', models.FileField(blank=True, upload_to='')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('C', 'Classic'), ('H', 'Happy'), ('S', 'Sad'), ('D', 'Devotional'), ('M', 'Melody')], max_length=1)),
                ('songs', models.FileField(blank=True, upload_to='')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.Movie')),
            ],
        ),
    ]

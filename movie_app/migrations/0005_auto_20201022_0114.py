# Generated by Django 2.2 on 2020-10-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_nowy_traktor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knn', models.IntegerField()),
                ('kmeans', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Nowy',
        ),
    ]

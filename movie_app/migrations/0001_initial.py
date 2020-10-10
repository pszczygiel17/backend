# Generated by Django 2.2 on 2020-10-09 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=100)),
                ('movie1', models.CharField(max_length=100)),
                ('movie2', models.CharField(max_length=100)),
                ('movie3', models.CharField(max_length=100)),
                ('elem1', models.CharField(max_length=100)),
                ('elem2', models.CharField(max_length=100)),
                ('elem3', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('country1', models.CharField(max_length=100)),
                ('country2', models.CharField(max_length=100)),
                ('country3', models.CharField(max_length=100)),
                ('actor1', models.CharField(max_length=100)),
                ('actor2', models.CharField(max_length=100)),
                ('actor3', models.CharField(max_length=100)),
                ('director1', models.CharField(max_length=100)),
                ('director2', models.CharField(max_length=100)),
                ('director3', models.CharField(max_length=100)),
                ('oscar', models.BooleanField()),
                ('years1', models.CharField(max_length=100)),
                ('years2', models.CharField(max_length=100)),
                ('years3', models.CharField(max_length=100)),
                ('food1', models.CharField(max_length=100)),
                ('food2', models.CharField(max_length=100)),
                ('food3', models.CharField(max_length=100)),
                ('group', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProfileDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=600)),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-25 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_actor_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(db_table='actors_movies', to='movies.Movie'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_alter_players_height_alter_players_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='height',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]

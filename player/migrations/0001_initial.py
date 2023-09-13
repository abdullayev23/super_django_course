# Generated by Django 4.2.5 on 2023-09-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('player', models.CharField(blank=True, max_length=100)),
                ('role', models.CharField(blank=True, max_length=100)),
                ('dr', models.DateField(blank=True)),
                ('height', models.PositiveIntegerField(default=0)),
                ('weight', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
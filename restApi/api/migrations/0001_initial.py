# Generated by Django 4.0.4 on 2022-06-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('capitulos', models.IntegerField()),
                ('imagen', models.CharField(max_length=250)),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2022-05-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('capitulos', models.CharField(max_length=10)),
                ('imagen', models.CharField(max_length=250)),
            ],
        ),
    ]
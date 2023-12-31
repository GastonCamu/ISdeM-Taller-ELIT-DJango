# Generated by Django 4.2.4 on 2023-09-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('tecnologias', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=150)),
                ('imagen', models.FilePathField(path='/img')),
            ],
        ),
    ]

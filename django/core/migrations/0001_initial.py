# Generated by Django 3.0.5 on 2020-04-06 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('caracteristica', models.CharField(max_length=200, verbose_name='Caracteristica')),
                ('dataperdido', models.DateTimeField(unique_for_date=10, verbose_name='Data perdido')),
            ],
        ),
    ]

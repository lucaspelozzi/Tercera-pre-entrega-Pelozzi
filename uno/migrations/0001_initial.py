# Generated by Django 4.2 on 2023-04-18 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MiModelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo1', models.CharField(max_length=50)),
                ('campo2', models.CharField(max_length=50)),
                ('campo3', models.CharField(max_length=50)),
                ('campo4', models.CharField(max_length=50)),
            ],
        ),
    ]

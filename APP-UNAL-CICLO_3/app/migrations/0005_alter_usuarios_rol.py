# Generated by Django 4.1.1 on 2022-10-07 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_usuarios_rol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='rol',
            field=models.CharField(max_length=50),
        ),
    ]

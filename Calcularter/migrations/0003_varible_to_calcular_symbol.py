# Generated by Django 3.0 on 2020-02-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calcularter', '0002_auto_20200224_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='varible_to_calcular',
            name='Symbol',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

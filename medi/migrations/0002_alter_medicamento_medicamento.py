# Generated by Django 4.0.3 on 2022-03-24 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='medicamento',
            field=models.TextField(unique=True),
        ),
    ]

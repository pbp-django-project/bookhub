# Generated by Django 4.2.5 on 2023-10-26 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
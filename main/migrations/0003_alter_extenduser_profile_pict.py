# Generated by Django 4.1.4 on 2023-10-29 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_extenduser_profile_pict'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='profile_pict',
            field=models.URLField(blank=True, default='https://www.personality-insights.com/wp-content/uploads/2017/12/default-profile-pic-e1513291410505.jpg', null=True),
        ),
    ]

# Generated by Django 3.0.8 on 2020-10-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbibi', '0007_auto_20201013_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]

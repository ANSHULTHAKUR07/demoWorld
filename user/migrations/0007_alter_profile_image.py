# Generated by Django 4.2.3 on 2023-09-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='profile_pics'),
        ),
    ]

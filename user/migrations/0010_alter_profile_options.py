# Generated by Django 4.2.3 on 2023-09-19 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_shoppinguser_friends'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': (('show_profile', 'only login user show profile page '),)},
        ),
    ]

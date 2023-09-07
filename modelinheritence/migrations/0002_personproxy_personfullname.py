# Generated by Django 4.2.3 on 2023-08-04 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelinheritence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonProxy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PersonFullName',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('modelinheritence.personproxy',),
        ),
    ]

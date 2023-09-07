# Generated by Django 4.2.3 on 2023-07-26 05:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cimage', models.ImageField(upload_to='images/categoryImages')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=50)),
                ('pprice', models.IntegerField()),
                ('pdesc', models.TextField(max_length=150)),
                ('pimage', models.ImageField(upload_to='images/productImages')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('pcat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FashionWorld.category')),
            ],
            options={
                'verbose_name': 'products',
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('p', 'pending'), ('c', 'completed')], max_length=50)),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FashionWorld.product')),
            ],
            options={
                'verbose_name': 'order',
                'db_table': 'order',
            },
        ),
    ]

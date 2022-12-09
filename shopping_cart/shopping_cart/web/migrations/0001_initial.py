# Generated by Django 4.1.3 on 2022-12-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.URLField()),
                ('price', models.FloatField()),
                ('product_type', models.CharField(max_length=30)),
                ('details', models.CharField(max_length=80)),
            ],
        ),
    ]

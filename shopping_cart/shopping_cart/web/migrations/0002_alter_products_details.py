# Generated by Django 4.1.3 on 2022-12-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='details',
            field=models.CharField(max_length=200),
        ),
    ]

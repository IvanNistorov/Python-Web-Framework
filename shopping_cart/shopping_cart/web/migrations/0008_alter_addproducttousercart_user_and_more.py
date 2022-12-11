# Generated by Django 4.1.3 on 2022-12-09 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0007_removeproducttousercart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproducttousercart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='RemoveProductToUserCart',
        ),
    ]

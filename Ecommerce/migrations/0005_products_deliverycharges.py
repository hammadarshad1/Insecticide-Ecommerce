# Generated by Django 2.2.6 on 2019-12-08 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0004_auto_20191205_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='deliveryCharges',
            field=models.FloatField(default=100.0),
            preserve_default=False,
        ),
    ]

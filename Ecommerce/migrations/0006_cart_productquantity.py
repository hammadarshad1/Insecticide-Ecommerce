# Generated by Django 2.2.6 on 2019-12-08 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0005_products_deliverycharges'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='productQuantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.6 on 2019-12-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0015_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderQuantity',
            field=models.IntegerField(null=True),
        ),
    ]

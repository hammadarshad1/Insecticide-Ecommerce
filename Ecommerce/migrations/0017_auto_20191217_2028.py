# Generated by Django 2.2.6 on 2019-12-17 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0016_auto_20191217_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderQuantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

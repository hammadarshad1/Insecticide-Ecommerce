# Generated by Django 2.2.6 on 2019-12-15 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0007_auto_20191215_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='productCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ecommerce.Category'),
        ),
    ]

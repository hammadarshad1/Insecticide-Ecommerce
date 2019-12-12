# Generated by Django 2.2.6 on 2019-12-05 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ecommerce', '0003_auto_20191205_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sliderimage',
            name='userId',
        ),
        migrations.AddField(
            model_name='cart',
            name='userId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

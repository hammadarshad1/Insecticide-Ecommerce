# Generated by Django 2.2.6 on 2019-12-12 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='parent_id',
        ),
    ]

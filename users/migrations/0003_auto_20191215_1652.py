# Generated by Django 2.2.6 on 2019-12-15 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_parent_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('genderId', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Gender'),
        ),
    ]

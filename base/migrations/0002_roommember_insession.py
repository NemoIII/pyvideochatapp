# Generated by Django 4.0.1 on 2022-03-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roommember',
            name='insession',
            field=models.BooleanField(default=True),
        ),
    ]
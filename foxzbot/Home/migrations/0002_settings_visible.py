# Generated by Django 4.1.3 on 2023-01-07 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
# Generated by Django 4.1.3 on 2023-03-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_settings_inputtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]

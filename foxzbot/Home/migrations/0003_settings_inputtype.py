# Generated by Django 4.1.3 on 2023-03-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_settings_app_alter_settings_key_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='inputType',
            field=models.CharField(default='text', max_length=20),
            preserve_default=False,
        ),
    ]
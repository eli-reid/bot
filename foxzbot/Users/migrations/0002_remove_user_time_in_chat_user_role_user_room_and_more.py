# Generated by Django 4.1.3 on 2023-01-07 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='time_in_chat',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.TextField(choices=[('d', 'D')], default='d'),
        ),
        migrations.AddField(
            model_name='user',
            name='room',
            field=models.TextField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.TextField(max_length=20),
        ),
    ]

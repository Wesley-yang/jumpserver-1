# Generated by Django 3.1.6 on 2021-06-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0073_auto_20210606_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemuser',
            name='assets',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='admin_user',
            new_name='_admin_user',
        ),
        migrations.AddField(
            model_name='systemuser',
            name='assets',
            field=models.ManyToManyField(blank=True, related_name='system_users', through='assets.AuthBook', to='assets.Asset', verbose_name='Assets'),
        ),
    ]

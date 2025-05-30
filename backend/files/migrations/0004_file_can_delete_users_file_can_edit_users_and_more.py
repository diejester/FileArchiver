# Generated by Django 5.2 on 2025-04-10 07:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_filepermission'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='can_delete_users',
            field=models.ManyToManyField(blank=True, related_name='can_delete_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='can_edit_users',
            field=models.ManyToManyField(blank=True, related_name='can_edit_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='file',
            name='can_view_users',
            field=models.ManyToManyField(blank=True, related_name='can_view_files', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='FilePermission',
        ),
    ]

# Generated by Django 5.2 on 2025-04-10 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='metadata',
            field=models.JSONField(null=True, verbose_name='Дополнительная информация к фото'),
        ),
    ]

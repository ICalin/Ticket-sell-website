# Generated by Django 4.2.1 on 2023-05-29 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.CharField(default='Nijmegen', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]

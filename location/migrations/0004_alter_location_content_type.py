# Generated by Django 4.2.1 on 2023-06-01 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('location', '0003_location_content_type_location_object_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
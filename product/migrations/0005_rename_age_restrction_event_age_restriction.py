# Generated by Django 4.2.1 on 2023-05-29 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_datetime_event_start_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='age_restrction',
            new_name='age_restriction',
        ),
    ]

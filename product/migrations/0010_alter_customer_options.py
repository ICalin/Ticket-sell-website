# Generated by Django 4.2.1 on 2023-06-04 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_eventcreator'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['user__first_name', 'user__last_name'], 'permissions': [('view_history', 'Can view history')]},
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-14 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_rename_product_anthonyoffense_offense'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Offense',
        ),
    ]

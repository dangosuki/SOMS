# Generated by Django 5.0.4 on 2024-04-13 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_anthonystudent_guardian'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anthonyoffense',
            old_name='product',
            new_name='offense',
        ),
    ]

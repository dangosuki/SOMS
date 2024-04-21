# Generated by Django 5.0.4 on 2024-04-13 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_anthonyproduct_anthonytag_anthonyorder_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Anthony',
            new_name='AnthonyStudent',
        ),
        migrations.RemoveField(
            model_name='anthonyproduct',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.DeleteModel(
            name='AnthonyOrder',
        ),
        migrations.DeleteModel(
            name='AnthonyProduct',
        ),
        migrations.DeleteModel(
            name='AnthonyTag',
        ),
    ]

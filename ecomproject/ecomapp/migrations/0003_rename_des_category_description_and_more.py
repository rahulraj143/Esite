# Generated by Django 4.1.5 on 2023-01-17 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0002_rename_availablity_product_available_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='des',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='des',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='update',
            new_name='updated',
        ),
    ]
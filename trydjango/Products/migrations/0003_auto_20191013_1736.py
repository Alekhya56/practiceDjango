# Generated by Django 2.2.6 on 2019-10-13 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_auto_20191012_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_model',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product_model',
            old_name='Price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product_model',
            old_name='Summary',
            new_name='summary',
        ),
        migrations.RenameField(
            model_name='product_model',
            old_name='Title',
            new_name='title',
        ),
    ]
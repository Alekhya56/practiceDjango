# Generated by Django 2.2.6 on 2019-10-25 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191025_0746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articalmodel',
            old_name='artical',
            new_name='artical_name',
        ),
        migrations.RenameField(
            model_name='articalmodel',
            old_name='author',
            new_name='author_name',
        ),
    ]

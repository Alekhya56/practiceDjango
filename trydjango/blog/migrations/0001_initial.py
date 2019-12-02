# Generated by Django 2.2.6 on 2019-10-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artical', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
    ]

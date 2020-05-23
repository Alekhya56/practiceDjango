# Generated by Django 2.2.6 on 2019-10-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('desc', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='pics')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
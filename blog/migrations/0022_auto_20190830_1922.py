# Generated by Django 2.2.4 on 2019-08-30 16:22

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190830_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]

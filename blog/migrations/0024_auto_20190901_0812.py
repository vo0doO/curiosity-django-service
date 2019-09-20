# Generated by Django 2.2.4 on 2019-09-01 05:12

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190831_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='author',
            new_name='author_ip',
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Как Вас зовут ?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Введите ваш телефон'),
        ),
    ]

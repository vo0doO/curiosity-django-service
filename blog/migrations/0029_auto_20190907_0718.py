# Generated by Django 2.2.4 on 2019-09-07 04:18

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20190903_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='zalogi',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Есть'), (2, 'Нет')], max_length=3, verbose_name='Есть ли у Вас имущество в залоге ?            Например, ипотечная квартира или                автомобиль купленный в автокредит.'),
        ),
    ]

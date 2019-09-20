# Generated by Django 2.2.4 on 2019-08-30 16:18

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190829_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='komu',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Банкам', 'Банкам'), ('Часным лица', 'Часным лица'), ('Судебным приставам', 'Судебным приставам'), ('Микрофинансовым организациям', 'Микрофинансовым организациям'), ('Другое', 'Другое')], max_length=73, verbose_name='Кому Вы должны ?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Как Вас зовут ?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='answer',
            name='prosrochky',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Нет'), (2, 'Да, до месяца'), (1, 'Да, от месяца до трёх'), (1, 'Более трёх месяцев')], max_length=7, verbose_name='Есть ли у Вас просрочки по кредитам ?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='skolko',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'До 200 000 руб'), (2, 'От 200 000 руб до 500 000 руб'), (3, 'От 500 000 руб до 1 000 000 руб'), (4, 'Более 1 000 000 руб'), (5, 'Более 5 000 000 руб')], max_length=9, verbose_name='Сколько всего Вы должны ?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='zalogi',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Есть'), (2, 'Нет')], max_length=3, verbose_name='Есть ли у Вас имущество в залоге ? Например, ипотечная квартира или автомобиль купленный в автокредит.'),
        ),
    ]

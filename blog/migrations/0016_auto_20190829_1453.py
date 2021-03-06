# Generated by Django 2.2.4 on 2019-08-29 11:53

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190829_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='komu',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Банкам', 'Банкам'), ('Часным лица', 'Часным лица'), ('Судебным приставам', 'Судебным приставам'), ('МФО', 'МФО'), ('Другое', 'Другое')], max_length=48, verbose_name='Кому вы должны ?'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='skolko',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'До 200 000 руб'), (2, 'От 200 000 руб до 500 000 руб'), (3, 'От 500 000 руб до 1 000 000 руб'), (4, 'Более 1 000 000 руб'), (5, 'Более 5 000 000 руб')], max_length=500, verbose_name='Сколько всего вы должны ?'),
        ),
    ]

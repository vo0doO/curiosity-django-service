# Generated by Django 2.2.4 on 2019-08-28 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_answer1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer1',
            name='choises',
        ),
        migrations.AddField(
            model_name='answer1',
            name='choices',
            field=models.ManyToManyField(to='blog.Choices'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-09-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developenv', '0002_command_is_accept'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='小车编号'),
        ),
    ]

# Generated by Django 2.0.7 on 2018-09-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('developenv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='command',
            name='is_accept',
            field=models.CharField(default=0, max_length=1, verbose_name='是否接受'),
            preserve_default=False,
        ),
    ]

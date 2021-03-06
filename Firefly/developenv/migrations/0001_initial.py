# Generated by Django 2.0.7 on 2018-09-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=10, verbose_name='唯一标识ID')),
                ('goal', models.CharField(max_length=10, verbose_name='目标地址代码')),
                ('path_start', models.CharField(max_length=10)),
                ('path_end', models.CharField(max_length=10)),
                ('box', models.CharField(max_length=255)),
                ('created_time', models.DateField(auto_now=True)),
                ('nav_status', models.CharField(max_length=10)),
                ('nav_service', models.CharField(max_length=10)),
                ('nav_location', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'carstatus',
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='小车编号')),
                ('type', models.CharField(max_length=1, verbose_name='命令类型')),
                ('param_1', models.CharField(max_length=1, verbose_name='参数1')),
                ('param_2', models.CharField(max_length=1, verbose_name='参数2')),
            ],
            options={
                'db_table': 'command',
            },
        ),
    ]

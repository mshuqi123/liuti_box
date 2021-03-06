# Generated by Django 2.2.4 on 2019-11-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emmagee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='文件名称')),
                ('files', models.FileField(unique=True, upload_to='emmagee', verbose_name='文件路径')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': 'Emmagee数据处理',
                'verbose_name_plural': 'Emmagee数据处理',
                'db_table': 'box_emmagee',
            },
        ),
    ]

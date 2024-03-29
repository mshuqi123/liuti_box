# Generated by Django 2.2.4 on 2020-06-10 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('value', models.CharField(default='', max_length=100, primary_key=True, serialize=False, unique=True, verbose_name='分桶名称')),
                ('describe', models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='分桶策略描述')),
                ('state', models.CharField(choices=[('J', '禁用'), ('Q', '启用')], default='Q', max_length=10, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '分桶策略',
                'verbose_name_plural': '分桶策略',
                'db_table': 'hlz_bucket',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yid', models.IntegerField(default='', unique=True, verbose_name='用户yid')),
                ('phone', models.IntegerField(blank=True, default='', null=True, unique=True, verbose_name='手机号')),
                ('cash_balance', models.FloatField(blank=True, default='', null=True, verbose_name='现金余额')),
                ('gold_coin_balance', models.FloatField(blank=True, default='', null=True, verbose_name='金币余额')),
                ('tongdun_decision', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='同盾状态')),
                ('user_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='用户姓名')),
                ('num_id', models.IntegerField(blank=True, default='', null=True, verbose_name='身份证号')),
                ('alipay', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='支付宝号')),
                ('channel', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='渠道号')),
                ('edition', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='注册版本号')),
                ('wechat_open_id', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='微信openid')),
                ('wechat_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='微信昵称')),
                ('tourist', models.BooleanField(default='', max_length=100, verbose_name='是否是游客')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后登陆时间')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
                'db_table': 'hlz_user',
            },
        ),
        migrations.CreateModel(
            name='User_bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default='', verbose_name='用户id')),
                ('value', models.CharField(default='', max_length=100, verbose_name='分桶名称')),
                ('num', models.IntegerField(default='', verbose_name='桶号')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '用户桶号',
                'verbose_name_plural': '用户桶号',
                'db_table': 'hlz_user_bucket',
            },
        ),
        migrations.CreateModel(
            name='User_equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default='', verbose_name='用户id')),
                ('value', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='设备id')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后更新时间')),
            ],
            options={
                'verbose_name': '设备信息',
                'verbose_name_plural': '设备信息',
                'db_table': 'hlz_equipment',
            },
        ),
    ]

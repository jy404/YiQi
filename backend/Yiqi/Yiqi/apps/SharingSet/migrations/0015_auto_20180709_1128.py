# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-09 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SharingSet', '0014_auto_20180708_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharingsetmodel',
            name='imageUrl',
            field=models.ImageField(blank=True, null=True, upload_to='SharingSet/%y/%d/6c7d323a74854545bd0783282cc0b00d', verbose_name='分享图片'),
        ),
        migrations.AlterField(
            model_name='sharingsetmodel',
            name='set_path',
            field=models.CharField(choices=[('0', '通用页面'), ('1', '活动页面'), ('5', '内容页面'), ('2', '发布页面'), ('4', '消息页面'), ('3', '发现页面')], default='0', max_length=1, verbose_name='分享页面设置'),
        ),
    ]

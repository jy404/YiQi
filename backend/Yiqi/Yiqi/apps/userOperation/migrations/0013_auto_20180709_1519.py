# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-09 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userOperation', '0012_auto_20180709_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysmessages',
            name='ISOPEN',
            field=models.CharField(choices=[('0', '未读'), ('1', '已读')], default='0', max_length=1, verbose_name='是否已读'),
        ),
        migrations.AlterField(
            model_name='activityuserinfo',
            name='type',
            field=models.CharField(choices=[('0', '活动发起人'), ('1', '活动参加人')], default='1', max_length=1, verbose_name='报名用户类型'),
        ),
        migrations.AlterField(
            model_name='feedbackmodels',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='FeedBackModels/%y/%d/72bf82e5896a4829bf2e5e680ab3d854', verbose_name='反馈图片'),
        ),
    ]

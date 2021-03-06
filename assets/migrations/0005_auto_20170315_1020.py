# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-15 10:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0004_auto_20170308_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='\u673a\u67dc\u7f16\u53f7')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u673a\u67dc',
                'verbose_name_plural': '\u673a\u67dc',
            },
        ),
        migrations.CreateModel(
            name='IDCLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
                ('comment', models.TextField(verbose_name='\u63cf\u8ff0')),
            ],
            options={
                'verbose_name': '\u673a\u623f\u7b49\u7ea7',
                'verbose_name_plural': '\u673a\u623f\u7b49\u7ea7',
            },
        ),
        migrations.CreateModel(
            name='ISP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='\u540d\u79f0')),
            ],
            options={
                'verbose_name': 'ISP\u7c7b\u578b',
                'verbose_name_plural': 'ISP\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='idc',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u673a\u623f\u5730\u5740'),
        ),
        migrations.AddField(
            model_name='idc',
            name='bandwidth',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u673a\u623f\u5e26\u5bbd'),
        ),
        migrations.AddField(
            model_name='idc',
            name='contacts',
            field=models.CharField(max_length=255, null=True, verbose_name='\u8054\u7cfb\u4eba'),
        ),
        migrations.AddField(
            model_name='idc',
            name='create_time',
            field=models.DateField(auto_now=True, default=datetime.datetime(2017, 3, 15, 10, 18, 47, 182000), verbose_name='\u521b\u5efa\u65f6\u95f4'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='eventlog',
            name='component',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='\u4e8b\u4ef6\u5b50\u9879'),
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.IDC', verbose_name='\u673a\u623f'),
        ),
        migrations.AddField(
            model_name='idc',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assets.ISP', verbose_name='ISP\u7c7b\u578b'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='idc',
            name='type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assets.IDCLevel', verbose_name='\u673a\u623f\u7c7b\u578b'),
            preserve_default=False,
        ),
    ]

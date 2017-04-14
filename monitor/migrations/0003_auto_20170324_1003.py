# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-24 10:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20170324_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u4e3b\u673a\u7ec4\u540d')),
                ('flags', models.IntegerField(verbose_name='\u6807\u8bb0')),
                ('groupid', models.IntegerField(verbose_name='\u4e3b\u673a\u7ec4id')),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u7ec4',
                'verbose_name_plural': '\u4e3b\u673a\u7ec4',
            },
        ),
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='\u6a21\u677f\u540d')),
                ('flags', models.IntegerField(verbose_name='\u6807\u8bb0')),
                ('templateid', models.IntegerField(verbose_name='\u6a21\u677fid')),
            ],
            options={
                'verbose_name': '\u6a21\u677f',
                'verbose_name_plural': '\u6a21\u677f',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='hostgroup_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='monitor.HostGroups', verbose_name='\u4e3b\u673a\u7ec4id'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='host',
            name='template_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='monitor.Templates', verbose_name='\u6a21\u677fid'),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-21 09:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('client', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('server', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('request', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('response', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
            ],
            options={
                'db_table': 'httplog',
            },
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 03:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170625_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='imagem',
            new_name='image',
        ),
    ]
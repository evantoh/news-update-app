# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-20 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180220_1430'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pud_date',
            new_name='pub_date',
        ),
    ]

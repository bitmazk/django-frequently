# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequently', '0002_auto_20150911_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', blank=True),
        ),
    ]

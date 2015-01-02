# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(unique=True, max_length=200),
        ),
    ]

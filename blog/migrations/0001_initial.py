# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
                ('yaratilma_tarihi', models.DateTimeField(null=True, blank=True)),
                ('yazar', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

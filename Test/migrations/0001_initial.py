# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('test_date', models.DateTimeField()),
                ('test_mode', models.CharField(max_length=1, choices=[('1', 'SLAM'), ('2', 'SSA')])),
                ('test_data', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tester',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('job', models.CharField(max_length=20)),
            ],
        ),
    ]

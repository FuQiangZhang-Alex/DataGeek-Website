# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-25 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogTags',
            fields=[
                ('tagid', models.UUIDField(default=uuid.UUID('d1c7d64f-0d12-4196-ade5-0b3ab28ca46a'), editable=False, primary_key=True, serialize=False)),
                ('tagname', models.CharField(max_length=50)),
                ('tagdes', models.CharField(max_length=250)),
                ('createts', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': False,
                'db_table': 'dg"."artical_tags',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.UUIDField(default=uuid.UUID('30176055-83ca-4caa-a04e-263706c87a1f'), editable=False, primary_key=True, serialize=False)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'managed': False,
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userid', models.UUIDField(default=uuid.UUID('b28f1179-8d26-464f-b603-a3221926a8dd'), editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'managed': False,
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Articals',
            fields=[
                ('artical_id', models.UUIDField(default=uuid.UUID('18664574-b3d2-41a0-b28d-47edce14468c'), editable=False, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='blogapi.Users')),
            ],
        ),
    ]

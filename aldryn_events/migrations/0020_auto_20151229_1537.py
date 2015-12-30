# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('aldryn_events', '0019_auto_20150804_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestEventsPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('total_count', models.PositiveIntegerField(default=3, help_text='Maximum count of events to display.')),
                ('app_config', models.ForeignKey(verbose_name='app_config', to='aldryn_events.EventsConfig')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='language_code',
            field=models.CharField(default=b'en', max_length=32, choices=[[b'en', b'English'], [b'ar', b'Arabic']]),
        ),
    ]

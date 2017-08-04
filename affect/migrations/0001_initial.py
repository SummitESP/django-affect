# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields.json


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(help_text=b'Name used when storing cookie for criteria decisions.', unique=True)),
                ('persistent', models.BooleanField(default=False, help_text=b'This criteria is persistant to the user, and a cookie will be set. Set off to evaluate criteria for user on each request.')),
                ('max_cookie_age', models.IntegerField(default=2592000, help_text=b'If this criteria is persistant, this is the amount of time in seconds before the cookie should expire. 0 or blank expires at end of browser session.', null=True, blank=True)),
                ('everyone', models.NullBooleanField(help_text=b'Turn criteria on (True) or off (False) for all users. Overrides ALL other criteria.')),
                ('testing', models.BooleanField(default=False, help_text=b'Allow this criteria to be set for a session for user testing.')),
                ('percent', models.DecimalField(help_text=b'A number between 0.0 and 99.9 to indicate a percentage of users for whom flags will be active.', null=True, max_digits=3, decimal_places=1, blank=True)),
                ('superusers', models.BooleanField(default=True, help_text=b'Activate this criteria for superusers?')),
                ('staff', models.BooleanField(default=False, help_text=b'Activate this criteria for staff?')),
                ('authenticated', models.BooleanField(default=False, help_text=b'Activate this criteria for authenticate users?')),
                ('device_type', models.IntegerField(default=0, help_text=b"Activate this criteria for users using certain classes of device. (NOTICE: This is only an attempt as device detection is hard and generally a bad idea. If you're doing something client-side, use css and js feature detection instead)", choices=[(0, b'Unknown'), (1, b'Desktop'), (2, b'Mobile'), (4, b'Dumb Phone')])),
                ('entry_url', models.TextField(default=b'', help_text=b'Activate this criteria for users who enter on one of these urls (comma separated list)', blank=True)),
                ('referrer', models.TextField(default=b'', help_text=b'Activate this criteria for users who entered from one of these domains (comma separated list)', blank=True)),
                ('query_args', django_extensions.db.fields.json.JSONField(default=None, help_text=b'Dictionary of key value pairs to expect in the querystring.(ie. {"foo": "bar"} matches ?foo=bar; {"foo": "*"} matches ?foo=<any value>; {"foo": ["bar", "baz"] matches ?foo=bar or ?foo=baz)', null=True, blank=True)),
                ('note', models.TextField(help_text=b'Note where this criteria is used.', blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Date when this criteria was created.', editable=False, db_index=True)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Date when this criteria was last modified.', editable=False)),
            ],
            options={
                'verbose_name_plural': 'criteria',
            },
        ),
        migrations.CreateModel(
            name='Flag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.SlugField(help_text=b'Key that will be attached to the request', unique=True)),
                ('active', models.BooleanField(default=True)),
                ('priority', models.IntegerField(default=0, help_text=b'If flag conflicts with other flags, highest priority is applied (0 - low priority, 100 - high priority)')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Date when this flag was created.', editable=False, db_index=True)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, help_text=b'Date when this flag was last modified.', editable=False)),
                ('conflicts', models.ManyToManyField(help_text=b'Other flags that this flag conflicts with, highest priority is applied.', related_name='_flag_conflicts_+', to='affect.Flag', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='criteria',
            name='flags',
            field=models.ManyToManyField(help_text=b'Flags to activate when this criteria is True.', to='affect.Flag', blank=True),
        ),
        migrations.AddField(
            model_name='criteria',
            name='groups',
            field=models.ManyToManyField(help_text=b'Activate this criteria for these user groups.', to='auth.Group', blank=True),
        ),
        migrations.AddField(
            model_name='criteria',
            name='users',
            field=models.ManyToManyField(help_text=b'Activate this criteria for these users.', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]

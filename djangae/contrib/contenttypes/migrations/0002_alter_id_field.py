# -*- coding: utf-8 -*-
# Generated by Django 1.9.9.dev20170116170623 on 2017-01-16 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class AlterFieldInOtherApp(migrations.AlterField):
    """ Allows AlterField to be run on a field in a different app to the one in which the migration
        is defined by accepting an additional 'app_label' kwarg to the __init__ method.
    """

    def __init__(self, app_label, model_name, name, field, preserve_default=True):
        self.app_label = app_label
        self.model_name = model_name
        self.name = name
        self.field = field
        self.preserve_default = preserve_default

    def deconstruct(self):
        kwargs = {
            'app_label': self.app_label,
            'model_name': self.model_name,
            'name': self.name,
            'field': self.field,
        }
        if self.preserve_default is not True:
            kwargs['preserve_default'] = self.preserve_default
        return (
            self.__class__.__name__,
            [],
            kwargs
        )

    def state_forwards(self, app_label, state):
        app_label = self.app_label
        return super(AlterFieldInOtherApp, self).state_forwards(app_label, state)

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        app_label = self.app_label
        return super(AlterFieldInOtherApp, self).database_forwards(app_label, schema_editor, from_state, to_state)

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        app_label = self.app_label
        return super(AlterFieldInOtherApp, self).database_backwards(app_label, schema_editor, from_state, to_state)

    def describe(self):
        return "Alter field %s on %s in app " % (self.name, self.model_name, self.app_label)


class Migration(migrations.Migration):
    """ Migration that changes the `id` field in the DJANGO ContentType app, so that foreign keys
        which point to it will allow 64 bit ints.  This then allows those foreign keys to work
        with the IDs returned by our SimulatedContentTypeManager.
    """

    dependencies = [
        ('djangae_contenttypes', '0001_patch_contenttypes_migrations'),  # DJANGAE contenttypes
        ('contenttypes', '0001_initial'),  # DJANGO contenttypes
    ]

    operations = [
        AlterFieldInOtherApp(
            app_label='contenttypes',
            model_name='contenttype',
            name='id',
            field=models.BigIntegerField(auto_created=True, blank=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

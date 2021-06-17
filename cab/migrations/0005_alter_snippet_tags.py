# Generated by Django 3.2.4 on 2021-06-05 07:25

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('cab', '0004_auto_20210310_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='tags',
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text='A comma-separated list of tags.',
                through='taggit.TaggedItem',
                to='taggit.Tag',
                verbose_name='Tags'
            ),
        ),
    ]

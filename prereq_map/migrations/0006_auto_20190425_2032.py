# Generated by Django 2.1.7 on 2019-04-25 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prereq_map', '0005_auto_20190425_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursegraph',
            name='build_hash',
        ),
        migrations.RemoveField(
            model_name='curricgraph',
            name='build_hash',
        ),
        migrations.AddField(
            model_name='coursegraph',
            name='needs_rebuild',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='curricgraph',
            name='needs_rebuild',
            field=models.BooleanField(default=False),
        ),
    ]

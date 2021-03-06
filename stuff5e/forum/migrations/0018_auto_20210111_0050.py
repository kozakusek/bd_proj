# Generated by Django 3.0.5 on 2021-01-10 23:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_auto_20210111_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='feats',
            field=models.ManyToManyField(blank=True, null=True, related_name='character_feats', to='forum.Feat'),
        ),
        migrations.AlterField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(blank=True, null=True, related_name='character_spells', to='forum.Class'),
        ),
        migrations.AlterField(
            model_name='feat',
            name='bonuses',
            field=models.ManyToManyField(blank=True, null=True, related_name='feat_bonuses', to='forum.Bonus'),
        ),
        migrations.AlterField(
            model_name='feat',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='spell',
            name='m',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

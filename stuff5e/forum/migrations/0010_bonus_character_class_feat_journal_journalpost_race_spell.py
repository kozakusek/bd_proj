# Generated by Django 3.0.5 on 2021-01-03 20:43

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0009_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('STR', 'STR'), ('DEX', 'DEX'), ('CON', 'CON'), ('INT', 'INT'), ('WIS', 'WIS'), ('CHA', 'CHA')], max_length=10)),
                ('value', models.IntegerField(choices=[(-2, '-2'), (-1, '-1'), (1, '1'), (2, '2')])),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('desc', ckeditor.fields.RichTextField()),
                ('custom', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Spell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('level', models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9')])),
                ('time', models.CharField(choices=[('24 Hours', '24 Hours'), ('12 Hours', '12 Hours'), ('8 Hours', '8 Hours'), ('1 Hour', '1 Hour'), ('10 Minutes', '10 Minutes'), ('1 Minute', '1 Minute'), ('Action', 'Action'), ('Reaction', 'Reaction'), ('Bonus', 'Bonus')], max_length=100)),
                ('school', models.CharField(choices=[('Abjuration', 'Abjuration'), ('Conjuration', 'Conjuration'), ('Divination', 'Divination'), ('Enchantment', 'Enchantment'), ('Evocation', 'Evocation'), ('Illusion', 'Illusion'), ('Necromancy', 'Necromancy'), ('Transmutation', 'Transmutation')], max_length=100)),
                ('concentration', models.BooleanField(default=False)),
                ('ritual', models.BooleanField(default=False)),
                ('range', models.CharField(choices=[('Special', 'Special'), ('Unlimited', 'Unlimited'), ('500 miles', '500 miles'), ('Sight', 'Sight'), ('1 mile', '1 mile'), ('1000 feet', '1000 feet'), ('500 feet', '500 feet'), ('300 feet', '300 feet'), ('150 feet', '150 feet'), ('120 feet', '120 feet'), ('90 feet', '90 feet'), ('60 feet', '60 feet'), ('30 feet', '30 feet'), ('15 feet', '15 feet'), ('10 feet', '10 feet'), ('5 feet', '5 feet'), ('Touch', 'Touch'), ('Self', 'Self')], max_length=100)),
                ('v', models.BooleanField(default=False)),
                ('s', models.BooleanField(default=False)),
                ('m', models.CharField(max_length=100)),
                ('duration', models.CharField(choices=[('Instantaneous', 'Instantaneous'), ('1 Round', '1 Round'), ('1 Minute', '1 Minute'), ('10 Minutes', '10 Minutes'), ('1 Hour', '1 Hour'), ('8 Hours', '8 Hours'), ('24 Hours', '24 Hours'), ('Special', 'Special'), ('Permament', 'Permament')], max_length=100)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('custom', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('classes', models.ManyToManyField(related_name='class_spells', to='forum.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('size', models.CharField(choices=[('Tiny', 'Tiny'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')], max_length=100)),
                ('speed', models.IntegerField()),
                ('desc', ckeditor.fields.RichTextField()),
                ('custom', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bonuses', models.ManyToManyField(related_name='race_bonuses', to='forum.Bonus')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user_access', models.ManyToManyField(related_name='journal_acc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('prerequisite', models.CharField(default='-', max_length=100)),
                ('desc', models.TextField()),
                ('custom', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bonuses', models.ManyToManyField(related_name='feat_bonuses', to='forum.Bonus')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('story', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('starting_class', models.CharField(max_length=100)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('feats', models.ManyToManyField(related_name='character_feats', to='forum.Feat')),
                ('spells', models.ManyToManyField(related_name='character_spells', to='forum.Class')),
                ('user_access', models.ManyToManyField(related_name='character_acc', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

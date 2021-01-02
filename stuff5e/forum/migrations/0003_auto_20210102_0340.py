# Generated by Django 3.0.5 on 2021-01-02 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='None', max_length=100),
        ),
    ]

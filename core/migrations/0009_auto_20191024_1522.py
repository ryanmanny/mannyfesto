# Generated by Django 2.2.6 on 2019-10-24 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191024_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='htmlpost',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

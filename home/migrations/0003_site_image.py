# Generated by Django 2.1.3 on 2018-11-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20181112_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='image',
            field=models.CharField(default='', max_length=1024),
        ),
    ]

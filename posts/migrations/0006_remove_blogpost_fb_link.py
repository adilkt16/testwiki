# Generated by Django 4.1.5 on 2023-02-14 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_blogpost_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='fb_link',
        ),
    ]

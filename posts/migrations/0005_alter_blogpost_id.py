# Generated by Django 4.1.5 on 2023-02-03 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_blogpost_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

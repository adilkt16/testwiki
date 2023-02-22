# Generated by Django 4.1.5 on 2023-02-17 15:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_remove_blogpost_awards_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='main_description',
            field=models.CharField(max_length=10000, validators=[django.core.validators.MinLengthValidator(250)]),
        ),
    ]

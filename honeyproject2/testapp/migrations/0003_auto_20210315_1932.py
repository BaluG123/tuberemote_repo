# Generated by Django 2.1 on 2021-03-15 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='video',
        ),
    ]

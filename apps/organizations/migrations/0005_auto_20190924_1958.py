# Generated by Django 2.2 on 2019-09-24 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_remove_courseorg_is_classics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='calegory',
            new_name='category',
        ),
    ]

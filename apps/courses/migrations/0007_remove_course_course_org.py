# Generated by Django 2.2 on 2019-09-24 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20190924_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_org',
        ),
    ]
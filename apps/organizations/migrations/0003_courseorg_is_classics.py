# Generated by Django 2.2 on 2019-09-24 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0002_auto_20190924_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='is_classics',
            field=models.BooleanField(default=False, verbose_name='是否经典'),
        ),
    ]
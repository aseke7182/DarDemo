# Generated by Django 2.2.1 on 2019-05-13 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20190514_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='amount',
            new_name='amounts',
        ),
    ]

# Generated by Django 2.2.6 on 2020-07-12 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institute', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='name',
            new_name='title',
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-26 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_Application', '0002_rename_address_info_address_rename_email_info_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='name',
            new_name='username',
        ),
    ]

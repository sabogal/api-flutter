# Generated by Django 4.0.5 on 2023-03-03 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_remove_historicaluser_state_remove_user_state_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='Document',
            new_name='document',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='Document',
            new_name='document',
        ),
    ]

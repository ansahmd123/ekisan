# Generated by Django 4.1.7 on 2024-02-29 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0006_alter_farm_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='name',
            new_name='user',
        ),
    ]
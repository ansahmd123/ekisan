# Generated by Django 4.1.7 on 2024-02-29 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profilepic'),
        ('farmer', '0005_farm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
        ),
    ]

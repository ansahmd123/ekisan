# Generated by Django 4.1.7 on 2024-03-03 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_password'),
        ('dealer', '0004_dealerprofilepic'),
    ]

    operations = [
        migrations.AddField(
            model_name='bit',
            name='farmer_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
    ]

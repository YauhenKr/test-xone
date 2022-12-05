# Generated by Django 4.1.3 on 2022-11-23 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_user_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='account',
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]

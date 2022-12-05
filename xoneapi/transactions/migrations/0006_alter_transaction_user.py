# Generated by Django 4.1.3 on 2022-11-22 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_account_user_account'),
        ('transactions', '0005_alter_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='transactions', to='user.user'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transaction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='organization',
            field=models.CharField(max_length=100),
        ),
    ]
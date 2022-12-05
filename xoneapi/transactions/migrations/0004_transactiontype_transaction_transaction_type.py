# Generated by Django 4.1.3 on 2022-11-21 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_alter_transaction_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='transactions.transactiontype'),
        ),
    ]

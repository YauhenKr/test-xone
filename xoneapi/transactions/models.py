from django.db import models
from django.conf import settings


class Transaction(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    amount = models.FloatField()
    time_trans_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        'categories.UserCategory', on_delete=models.CASCADE
    )
    organization = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    transaction_type = models.ForeignKey('TransactionType', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.description}'


class TransactionType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'

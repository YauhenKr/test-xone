from django.contrib import admin

from transactions.models import Transaction, TransactionType


admin.site.register(Transaction)
admin.site.register(TransactionType)


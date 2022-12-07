from transactions.models import Transaction, TransactionType
from user.models import Account


def order_by(data, requested_user):
    if data['order_column'] == 'date':
        return Transaction.objects.filter(user=requested_user).order_by('time_trans_at')
    elif data['order_column'] == 'amount':
        return Transaction.objects.filter(user=requested_user).order_by('-amount')
    else:
        return Transaction.objects.filter(user=requested_user)


def create_transaction(user, data, category, transaction_type):
    Transaction.objects.create(
        user=user,
        amount=data['amount'],
        category=category,
        organization=data['organization'],
        transaction_type=transaction_type,
        description=data['description']
    )


def update_account(user, cash_flow, data):
    Account.objects.filter(user=user).update(
        user=user,
        balance=cash_flow
    )


def do_transaction(data, account):
    if data.get('transaction_type') == 1:
        return account.balance + data['amount']
    else:
        return account.balance - data['amount']


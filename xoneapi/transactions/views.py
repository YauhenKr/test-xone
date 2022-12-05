from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from transactions.models import Transaction, TransactionType
from user.models import User, Account
from categories.models import Category
from transactions.serializers import TransactionSerializer
from transactions.tasks import send_users_statistic


# list of transactions
class TransactionAPIView(APIView):
    class QueryParamsSerializer(serializers.Serializer):
        user = serializers.IntegerField()
        order_column = serializers.CharField(required=False)

    def get(self, request):
        serializer = self.QueryParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        requested_user = data['user']
        if data['order_column'] == 'date':
            users_statistic = Transaction.objects.filter(user=requested_user).order_by('time_trans_at')
        elif data['order_column'] == 'amount':
            users_statistic = Transaction.objects.filter(user=requested_user).order_by('-amount')
        else:
            users_statistic = Transaction.objects.filter(user=requested_user)

        send_users_statistic(users_statistic)

        return Response(
            TransactionSerializer(
                users_statistic, many=True).data, status=status.HTTP_200_OK)    # how to send email


# create a transaction
class TransactionCreateAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        description = serializers.CharField()
        user = serializers.IntegerField()
        amount = serializers.FloatField()
        category = serializers.IntegerField()
        organization = serializers.CharField()
        transaction_type = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        account = Account.objects.filter(user=data['user']).get()
        user = User.objects.get(pk=data['user'])
        category = Category.objects.get(pk=data['category'])
        transaction_type = TransactionType.objects.get(pk=data['transaction_type'])
        if data.get('transaction_type') == 1:
            cash_flow = account.balance + data['amount']
        else:
            cash_flow = account.balance - data['amount']

        transaction = Transaction.objects.create(
            user=user,
            amount=data['amount'],
            category=category,
            organization=data['organization'],
            transaction_type=transaction_type,
            description=data['description']
        )

        account_update = Account.objects.filter(user=data['user']).update(
            user=user,
            balance=cash_flow
        )

        return Response({'message': 'Transaction was done!'}, status=status.HTTP_201_CREATED)

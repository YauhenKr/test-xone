from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from transactions.services import (
    order_by, create_transaction, update_account,
    do_transaction
)
from transactions.models import Transaction, TransactionType
from transactions.serializers import TransactionSerializer
from transactions.tasks import send_users_statistic
from user.models import User, Account
from categories.models import UserCategory


class TransactionAPIView(APIView):
    class QueryParamsSerializer(serializers.Serializer):
        order_column = serializers.CharField(required=False)

    def get(self, request):
        serializer = self.QueryParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        requested_user = User.objects.get(user=request.user)
        users_statistic = order_by(data, requested_user)
        send_users_statistic(users_statistic)
        return Response(
            TransactionSerializer(
                users_statistic, many=True).data, status=status.HTTP_200_OK)


class TransactionCreateAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        description = serializers.CharField()
        amount = serializers.FloatField()
        category = serializers.IntegerField()
        organization = serializers.CharField()
        transaction_type = serializers.IntegerField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = User.objects.get(user=request.user)
        account = Account.objects.filter(user=user).get()
        category = UserCategory.objects.get(pk=data.get('category'))
        transaction_type = TransactionType.objects.get(pk=data['transaction_type'])
        cash_flow = do_transaction(data, account)
        create_transaction(user, data, category, transaction_type)
        update_account(user, cash_flow, data)
        return Response(
            {'message': 'Transaction was done!'},
            status=status.HTTP_201_CREATED
        )

from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response

from user.models import Account, User
from user.serializers import AccountSerializer


# user's balance
class UserBalanceAPIView(APIView):
    class QueryParamsSerializer(serializers.Serializer):
        user = serializers.IntegerField()

    def get(self, request):
        serializer = self.QueryParamsSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        account = Account.objects.filter(user=data['user'])
        return Response(AccountSerializer(account, many=True).data, status=status.HTTP_200_OK)


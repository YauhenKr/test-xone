from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from user.models import Account, User
from user.serializers import AccountSerializer


class UserBalanceAPIView(APIView):
    def get(self, request):
        user = User.objects.get(user=request.user)
        account = Account.objects.filter(user=user)
        return Response(
            AccountSerializer(account, many=True).data,
            status=status.HTTP_200_OK
        )

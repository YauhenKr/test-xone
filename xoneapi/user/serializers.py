from rest_framework.serializers import ModelSerializer

from user.models import User, Account


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user',
        ]


class AccountSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = [
            'balance',
            'user',
        ]




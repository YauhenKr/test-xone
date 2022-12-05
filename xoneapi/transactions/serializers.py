from rest_framework.serializers import ModelSerializer

from transactions.models import Transaction
from user.serializers import UserSerializer
from categories.serializers import CategorySerializer


class TransactionSerializer(ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Transaction
        fields = [
            'user',
            'amount',
            'time_trans_at',
            'category',
            'organization',
        ]
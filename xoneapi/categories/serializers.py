from rest_framework.serializers import ModelSerializer

from categories.models import Category, UserCategory
from user.serializers import UserSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name_of_category',
        ]


class UserCategorySerializer(ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = UserCategory
        fields = '__all__'

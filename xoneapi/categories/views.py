from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from categories.models import UserCategory, Category
from user.models import User


# create a new category
class CreateCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        category = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user_name = request.user
        user = User.objects.get(user=user_name)
        creating_category = Category.objects.filter(name_of_category=data['category'])
        if not creating_category.exists():
            creating_category = Category.objects.create(name_of_category=data['category'])
        else:
            creating_category = creating_category.get()
        UserCategory.objects.create(user=user, category=creating_category)
        return Response({'message': 'Category has been created!'}, status=status.HTTP_201_CREATED)


class DeleteCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        category = serializers.IntegerField()

    def delete(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        category = data['category']
        user_name = request.user
        user = User.objects.get(user=user_name)
        user_categories = user.categories.values_list('category_id', flat=True)
        if category not in user_categories:
            return Response({'message': 'Category has not been found!'}, status=status.HTTP_204_NO_CONTENT)
        UserCategory.objects.filter(user=user, category=category).delete()
        return Response({'message': 'Category has been deleted!'}, status=status.HTTP_204_NO_CONTENT)



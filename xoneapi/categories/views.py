from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from categories.services import (
    creating_category, get_user_categories_list, get_user, delete_category
)
from user.models import User


class CreateCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        category = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        user = User.objects.get(user=request.user)
        creating_category(user, data)
        return Response(
            {'message': 'Category has been created!'},
            status=status.HTTP_201_CREATED
        )


class DeleteCategoryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        category = serializers.IntegerField()

    def delete(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        category = data['category']
        user = User.objects.get(user=request.user)
        user_categories = get_user_categories_list(user, category)
        if category not in user_categories:
            return Response(
                {'message': 'Category has not been found!'},
                status=status.HTTP_204_NO_CONTENT
            )
        delete_category(user, category)
        return Response(
            {'message': 'Category has been deleted!'},
            status=status.HTTP_204_NO_CONTENT
        )

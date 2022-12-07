from django.urls import path

from categories.views import CreateCategoryAPIView, DeleteCategoryAPIView

urlpatterns = [
    path('create', CreateCategoryAPIView.as_view()),
    path('delete', DeleteCategoryAPIView.as_view()),
]

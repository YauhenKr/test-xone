from django.urls import path, include

from categories.views import CreateCategoryAPIView, DeleteCategoryAPIView

urlpatterns = [
    # create a new category
    path('create', CreateCategoryAPIView.as_view()),

    # delete a new category
    path('delete', DeleteCategoryAPIView.as_view()),
]

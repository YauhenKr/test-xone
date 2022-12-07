from django.urls import path

from user.views import UserBalanceAPIView

urlpatterns = [
    path('balance', UserBalanceAPIView.as_view()),
]

from django.urls import path, include

from user.views import UserBalanceAPIView

urlpatterns = [
    # path('', UserRegisterAPIView.as_view()),
    # user's balance
    path('balance', UserBalanceAPIView.as_view()),
]

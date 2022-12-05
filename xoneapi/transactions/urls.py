from django.urls import path, include

from transactions.views import TransactionCreateAPIView, TransactionAPIView

urlpatterns = [
    # create a transaction
    path('create', TransactionCreateAPIView.as_view()),
    # user's statistic
    path('statistic', TransactionAPIView.as_view()),
]

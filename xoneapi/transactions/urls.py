from django.urls import path, include

from transactions.views import TransactionCreateAPIView, TransactionAPIView

urlpatterns = [
    path('create', TransactionCreateAPIView.as_view()),
    path('statistic', TransactionAPIView.as_view()),
]

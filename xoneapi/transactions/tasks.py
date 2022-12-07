from django.core.mail import send_mail

from user.models import User
from xoneapi.celery import app


@app.task
def send_users_statistic(users_statistic):
    for user in User.objects.all():
        send_mail(
            'Дасылаем статыстыку',
            [users_statistic],
            'dejos47067@dmonies.com',
            ['YauhenDrums@yandex.ru'],
            fail_silently=False,
        )


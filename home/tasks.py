from celery import shared_task
from .models import Number
import time
from django.core.mail import send_mail


@shared_task
def adding(x, y, id):
	time.sleep(5)
	num = Number.objects.get(id=id)
	num.result = x + y
	num.save()
	return num.result


@shared_task
def show():
	send_mail('Test', 'This is a test email for django-celery-beat', 'mr.moshtaghi@gmail.com', ['mr.sajjad@gmail.com'])
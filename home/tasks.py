from celery import shared_task
from .models import Number
import time


@shared_task
def adding(x, y, id):
	time.sleep(20)
	num = Number.objects.get(id=id)
	num.result = x + y
	num.save()
	return num.result

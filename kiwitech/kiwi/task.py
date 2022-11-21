from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task

def sleepy(duration):
    sleepy(duration)
    return None



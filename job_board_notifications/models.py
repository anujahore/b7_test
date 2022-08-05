from django.db import models

# Create your models here.
from django.db.models.signals import pre_delete

from django.dispatch import receiver

from django.shortcuts import render

from job_board_main.models import Job, Subscriber, Subscription
from job_board_main.signals import new_subscriber

from django.core.mail import send_mail

# Create your views here.


@receiver(new_subscriber, sender=Subscription)
def handle_new_subscription(sender, **kwargs):
    print(' in handle_new_subscription')
    sub = kwargs['subscriber']
    job = kwargs['job']
    msg = f'''user {sub} has just Subscribed ton the job-{job}'''
    print(msg)
    
    send_mail(subject=f'New Subscription for {job.title}',
    message=msg,
    from_email= 'admin@jobnotify.com',
    recipient_list=[job.cpmpany_email],
    fail_silently=False)


@receiver(pre_delete, sender=Job)
def handle_deleted_job_posting(**kwargs):
    print('in handle_deleted_job_posting')
    job = kwargs['instance']
    # find the subscribes list
    sub = Subscription.objects.filter(job=job)
    for single_sub in sub:
        msg = f'Dear {Subscriber.email}, the job posting {job.title} by {job.company} has been down.'
        print(msg)

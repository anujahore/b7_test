from django.http import HttpResponse
from django.shortcuts import render

from .signals import new_subscriber

from .models import *

# Create your views here.

def get_jobs(request):
    '''
    get all jobs from db
    '''
    jobs = Job.objects.all()
    return render(request, 'jobs.html', {'jobs': jobs})


def get_job(request, id):
    '''
    this function is to get single job
    '''
    job = Job.objects.get(id=id)
    return render(request, 'job.html', {'job': job})

from django.db import transaction

def subscribe(request, id):
    '''
    this function is for subscribe
    '''
    if request.method == 'POST':
        with transaction.atomic():
            job = Job.objects.get(id=id)
            data = Subscriber.objects.filter(email=request.POST['email'])
            if data.exists():
                sub = data[0]
            else:
                sub = Subscriber(email=request.POST['email'])
                sub.save()
                subscription = Subscription(user=sub, job=job)
                new_subscriber.send(sender=Subscription, job=job, subscriber=sub)

                subscription.save()
                # new_subscriber.send(sender=Subscription, job=job, subscriber=sub)
                payload = {
                    'job': job,
                    'email': request.POST['email']
                }
                return render(request, 'subscribed.html', {'payload': payload})
    else:
        return HttpResponse('InValid reques...!')


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User) #--> post save -- user ke andar entry hogi then yeh code execute hoga
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# post_save.connect(create_user_profile, User) --> @receiver(post_save, sender=User) yacha substitute
from django.db import models

# Create your models here.


class Job(models.Model):
    company = models.CharField(max_length=255, blank=False)
    cpmpany_email = models.CharField(max_length=255, blank=False)
    title = models.CharField(max_length=255, blank=False)
    detail = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.title

class Subscriber(models.Model):
    email = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

class Subscription(models.Model):

  
    # email = models.CharField(max_length=255, blank=False, unique=True)
    user = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='subscriptions')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'job'),)







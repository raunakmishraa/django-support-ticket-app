from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from .functions import send_issue_status_email

status_choices=[
    ("Reported","Reported"),
    ("In Progress","In Progress"),
    ("Solved","Solved")
]

priority_choices=[
    ("Urgent","Urgent"),
    ("High","High"),
    ("Medium","Medium"),
    ("Low","Low")
]

now_time=timezone.now()

# Create your models here.
class custom_user_model(AbstractUser):
    phone=models.CharField('NUMBER',max_length=100,unique=True)
    is_email_verified=models.BooleanField('EMAIL VERIFIED', default=False)
    username=models.EmailField('EMAIL',unique=True,null=True)

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['phone','first_name','last_name']

class global_settings(models.Model):
    email=models.EmailField('Email:')
    phone=models.IntegerField('Number:')
    fb_link = models.CharField('FACEBOOK LINK:', max_length=250)
    insta_link = models.CharField('INSTAGRAM LINK:', max_length=250)

class ticket_model(models.Model):
    raised_by=models.EmailField('Raised By')
    subject=models.CharField('Subject',max_length=250)
    issue=models.CharField('Issue Details',max_length=500)
    priority=models.CharField('Priority',max_length=10,choices=priority_choices,null=True,blank=True)
    ticket_number=models.IntegerField('Ticket Number')
    status=models.CharField('Status',choices=status_choices,null=True,blank=True,max_length=30,default='Reported')
    created_at=models.DateTimeField('Created At',default=now_time)

    def save(self, *args, **kwargs):
        send_issue_status_email(self.raised_by,self.ticket_number,self.status,self.created_at)
        super().save(*args,**kwargs)
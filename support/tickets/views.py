message=''

from django.shortcuts import render,redirect
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
#from django.http import HttpResponse
from . import models
import random
from django.contrib.auth import get_user_model

# Global Variables
global_details=models.global_settings.objects.get(pk=1)
User=get_user_model()

# Data Fetching functions
def get_total_user_issue(request):
    email=request.user.username
    total_issues=models.ticket_model.objects.filter(raised_by=email).count()
    return total_issues

def get_inprogress_user_issue(request):
    email=request.user.username
    inprogress_issues=models.ticket_model.objects.filter(raised_by=email,status='In Progress').count()
    return inprogress_issues

def get_solved_user_issue(request):
    email=request.user.username
    solved_issues=models.ticket_model.objects.filter(raised_by=email,status='Solved').count()
    return solved_issues

# Views Functions
def indexPage(request):
    global message
    if request.method == "POST":
        if 'login_email' in request.POST:
            user_email=request.POST['login_email']
            user_pass=request.POST['login_password']
            user=authenticate(request,username=user_email,password=user_pass)
            #print(user,user_email,user_pass)
            if user is not None:
                login(request,user)
                message=f'You are logged in successfully as {user_email}'
                return redirect('dashboard/')
            else:
                message="Login credentials did not match. Please try again."
    if request.user.is_authenticated:
        return redirect('dashboard/')
    return render(request,'index.html',{'global':global_details,'message':message})

def dashboard(request):
    global message
    if request.user.is_authenticated:
        total_issues_no=get_total_user_issue(request)
        inprogress_issues_no=get_inprogress_user_issue(request)
        solved_issues_no=get_solved_user_issue(request)
        statistics={
            'raised_issues':total_issues_no,
            'inprogress_issues':inprogress_issues_no,
            'solved_issues':solved_issues_no
        }
        issues=models.ticket_model.objects.filter(raised_by=request.user.username).order_by('-created_at')[:5]
        return render(request,'dashboard.html',{'global':global_details,'message':message,'statistics':statistics,'issues':issues})
    else:
        message='Please login first to access your password.'
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/')

def raise_issue(request):
    global message
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'issue' in request.POST:
                email=request.user.username
                subject=request.POST['subject']
                issue=request.POST['issue']
                priority=request.POST['priority']
                ticket_no=random.randint(000000,999999)
                models.ticket_model.objects.create(raised_by=email,subject=subject,issue=issue,priority=priority,ticket_number=ticket_no)
                message=f"New issue raised successfully with ticket number: #{ticket_no}"
        return render(request,'raise_issue.html',{'global':global_details,'message':message})
    else:
        message="Please login first to raise an issue."
        return redirect('/')

def all_issues(request):
    global message
    if request.user.is_authenticated:
        issues=models.ticket_model.objects.filter(raised_by=request.user.username)
        return render(request,'all_issue.html',{'global':global_details,'message':message,'issues':issues})
    else:
        message="Please login first to see your issues list."
        return redirect('/')
    
def progress_issues(request):
    global message
    if request.user.is_authenticated:
        progress=models.ticket_model.objects.filter(raised_by=request.user.username,status='In Progress')
        return render(request,'all_issue.html',{'global':global_details,'message':message,'issues':progress})
    else:
        message="Please login first to see in progress issues list."
        return redirect('/')
    
def solved_issues(request):
    global message
    if request.user.is_authenticated:
        solved=models.ticket_model.objects.filter(raised_by=request.user.username,status='Solved')
        return render(request,'all_issue.html',{'global':global_details,'message':message,'issues':solved})
    else:
        message="Please login first to see solved issues list."
        return redirect('/')
    
def issue_details(request,ticket):
    global message
    if request.user.is_authenticated:
        issue=models.ticket_model.objects.filter(ticket_number=ticket)
        if issue.count() == 0:
            message='No issues found.'
            return redirect('/dashboard/')
        else:
            return render(request,'issue_details.html',{'global':global_details,'issue':issue.first()})
    else:
        message="Please login to access issue description."
        return redirect('/')
    
def change_password(request):
    global message
    if request.user.is_authenticated:
        if request.method == 'POST':
            new_pass=request.POST['new_pass']
            confirm_new_pass=request.POST['confirm_new_pass']
            if new_pass != confirm_new_pass:
                message='New Password and Confirm New Password did not match.'
            else:
                request_user=User.objects.get(username__exact=request.user.username)
                try:
                    request_user.set_password(new_pass)
                except Exception as e:
                    message=e
                request_user.save()
                message=f'Password for {request_user} changed successfully.'
        return render(request,'change_pass.html',{'global':global_details,'message':message})
    else:
        message='Please login first to change your password.'
        return redirect('/')
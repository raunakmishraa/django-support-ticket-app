from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('raise/', views.raise_issue, name='raise_issue'),
    path('issues/', views.all_issues, name='all_issues'),
    path('progress/', views.progress_issues, name='progress_issues'),
    path('solved/', views.solved_issues, name='solved_issues'),
    path('issue/<int:ticket>/', views.issue_details, name='issues_description'),
    path('password_change', views.change_password, name='password_change'),
]
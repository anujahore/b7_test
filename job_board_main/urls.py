
from django.urls import path
from job_board_main import views

urlpatterns = [
    # all jobs
    path('jobs/', views.get_jobs, name='get_jobs'),
    path('jobs/<int:id>/', views.get_job, name='get_job'),
    path('jobs/<int:id>/subscribe/', views.subscribe, name='subscribe'),
]
from django.urls import path

# from app.views import hello, job_detail
from app import views


urlpatterns = [
    path('', views.job_list, name="jobs_home"),
    path('hello/', views.hello, name='hello_display'),
    path('job/<int:id>', views.job_detail, name="jobs_detail"),
    # path("job/<str:id>", views.job_detail),
]

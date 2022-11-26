from django.urls import path
from applybank import views


urlpatterns = [
    path('applyform/', views.ApplyForm, name='apply-form')

]

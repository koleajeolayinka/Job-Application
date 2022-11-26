from django.urls import path
from applymode import views


urlpatterns = [
    path('applyform/', views.ApplyForm, name='apply-form'),
    path('form', views.ApplyForm, name='form'),

]

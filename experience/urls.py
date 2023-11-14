from django.urls import path
from experience import views

urlpatterns = [
    path('', views.experience_list, name='experience_list'),
    path('new/', views.experience_new, name='new'),
]
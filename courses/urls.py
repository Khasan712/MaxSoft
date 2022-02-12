from django.urls import path
from . import views


urlpatterns = [
    path('my-courses', views.courses, name='courses'),
    path('my-courses/<slug:slug>/', views.view_course, name='view_course'),
    path('my-modules/<slug:slug>/', views.view_module, name='view_module'),
]

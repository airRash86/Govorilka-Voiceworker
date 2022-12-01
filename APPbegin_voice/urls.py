from django.urls import path
from . import views

urlpatterns = [
    path('', views.pr),
    path('voiceworker/', views.index, name='voiceworker'),
    path('error/', views.errTooMuchChars,  name='errTooMuchChars'),
    path('TESTING/', views.TESTING, name='TESTING'),
    path('ready/<slug:DijArg>/', views.ready, name='ready'), 
  ]


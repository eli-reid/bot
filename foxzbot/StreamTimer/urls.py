from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.StreamTimerSettingsView.as_view(), name='StreamTimer.Control'),
    path('timer/<str:key>',views.StreamTimerView.as_view(), name='StreamTimer.View')
] 
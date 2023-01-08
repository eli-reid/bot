from django.urls import path

from . import views

urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    path('settings', views.SettingsView.as_view(), name='settings'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
] 
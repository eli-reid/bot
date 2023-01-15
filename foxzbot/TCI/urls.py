from django.urls import path

from . import views

urlpatterns = [ 
    path('stop', views.TCIStopView.as_view(), name='tcistop'),
    path('start', views.TCIStartView.as_view(), name='tcistart'),
] 
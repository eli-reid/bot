from django.urls import path
from . import views

urlpatterns = [ 
    path('<str:pk>', views.SettingsUpdateView.as_view(), name='settings.list'),
    path('add/', views.SettingsCreationView.as_view(),name='settings.add'),
    path('edit/<int:pk>', views.SettingsUpdateView.as_view(), name='settings.edit'),
    path('delete/<int:pk>', views.SettingsDeleteView.as_view(), name='settings.delete'),
    path('<int:pk>', views.SettingsDetailView.as_view(), name='settings.detail'),
]
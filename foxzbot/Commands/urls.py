from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.CommandListView.as_view(), name='command.list'),
    path('add/', views.CommandCreationView.as_view(), name='command.add'),
    path('edit/<int:pk>', views.CommandUpdateView.as_view(), name='command.edit'),
    path('delete/<int:pk>', views.CommandDeleteView.as_view(), name='command.delete'),
    path('<int:pk>', views.CommandDetailView.as_view(), name='command.detail'),
]
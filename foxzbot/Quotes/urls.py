from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.QuotesListView.as_view(), name='quotes.list'),
    path('add/', views.QuotesCreationView.as_view(),name='quote.add'),
    path('edit/<int:pk>', views.QuotesUpdateView.as_view(), name='quote.edit'),
    path('delete/<int:pk>', views.QuotesDeleteView.as_view(), name='quote.delete'),
    path('<int:pk>', views.QuotesDetailView.as_view(), name='quote.detail'),
]
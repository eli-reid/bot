from django.urls import path
from .views import APIOauth, GetCodeView
urlpatterns = [
    path("oauth/", APIOauth.as_view()),
    path("oauth/code",GetCodeView.as_view()),
]

from django.urls import path
from .views import APIOauth, GetCodeView, makeApiCall
urlpatterns = [
    path("oauth/", APIOauth.as_view()),
    path("oauth/code",GetCodeView.as_view()),
    path("apicall",makeApiCall.as_view() )

]

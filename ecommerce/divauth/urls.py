from django.urls import path
from divauth import views
urlpatterns = [
    path("signup/",views.signup,name='signup')
]

from django.urls import path
from divauth import views
urlpatterns = [
    path("signup/",views.signup,name='signup'),
    path("login/",views.login,name='login')
]

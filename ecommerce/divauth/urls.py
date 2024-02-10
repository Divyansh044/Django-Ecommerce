from django.urls import path
from divauth import views
urlpatterns = [
    path("signup/",views.signup,name='signup'),
    path("login/",views.login,name='login'),
    path('activate/<uidb64>/<token>/',views.ActivateAccountView.as_view(),name='activate')
]

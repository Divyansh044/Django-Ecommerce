from django.urls import path
from home import views
urlpatterns = [
    path("",views.home,name='home'),
    path('purchase',views.purchase,name='purchase'),
    path("men's",views.men,name="men's"),
    path("women's",views.women,name="women's"),
    path('cart',views.cart,name="cart"),
    path('checkout',views.checkout,name="checkout"),

]

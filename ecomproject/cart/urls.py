from django.urls import path
from . import views
app_name='cart'
urlpatterns = [
    path('',views.cartdet,name='cartdet'),
    path('addcart/<int:productid>/',views.addcart,name='addcart'),
    path('cartdel/<int:productid>/',views.cartdel,name='cartdel'),
    path('trash/<int:productid>/',views.trash,name='trash'),
]
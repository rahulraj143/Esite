from django.urls import path
from ecomapp import views
app_name='ecomapp'
urlpatterns = [
    path('',views.allProdCat,name='allProdCat'),
    path('products_by_category<slug:c_slug>/',views.allProdCat,name='products_by_category'),
    path('prodetail<slug:c_slug>/<slug:pro_slug>/',views.prodetail,name='prodetail'),

]
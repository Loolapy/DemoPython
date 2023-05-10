from django.urls import path
from . import views
app_name='Kite'

urlpatterns = [

    path('',views.AllProductCat,name='AllProductCat'),
    path('<slug:c_slug>/',views.AllProductCat,name='product_by_category'),
    path('<slug:c_slug>/<slug:products_slug>/', views.prodetail, name='productcategory'),

]
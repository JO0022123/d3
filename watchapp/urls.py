from .import views
from django.urls import path
from django.urls import re_path as url
urlpatterns=[
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("create",views.adddata,name="create"),
    url(r'delete/(?P<pk>[0-9]+)/$',views.delete,name="delete"),
 
    path("about/",views.about,name="about"),
    path('reg/',views.signup,name="reg"),
     path('login/',views.login,name="login"),
     path('logout/',views.logout,name="logout"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("update/<int:id>",views.update,name="update"),
    path("card/",views.card,name="card"),
    path("product/",views.productlog,name="product"),
    path("card/<str:pname>",views.product_details,name="product_details"),
    path('offer/',views.offer,name="offer"),
     path('addcart/',views.cart_page,name="cart_page"),
      path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
       path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
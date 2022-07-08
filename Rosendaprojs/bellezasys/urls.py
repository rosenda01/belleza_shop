from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [
    path('',views.Home, name="Home"),
    path('admin/', admin.site.urls),
    path('register/',views.createCustomer, name="Register"),
    path('createorder/',views.CreateOrder, name="CreateOrder"),
    path('products/',views.Products, name="Products"),
    path('reviewpage/',views.ReviewPage, name="ReviewPage"),
    path('createreview/',views.CreateReview, name="CreateReview"),
    path('loginpage/',views.loginPage, name="Login"),
    path('logout/',views.logoutUser, name="logoutUser"),
    path('ownerlogin/',views.OwnerLogin, name="OwnerLogin"),
    path('ownerdashboard/',views.OwnerDashboard, name="OwnerDashboard"),
    path('ownerproduct/',views.OwnerProduct, name="OwnerProduct"),
    path('ownerorder/',views.OwnerOrder, name="OwnerOrder"),
    path('cart/',views.Cart, name="Cart"),
    path('addproduct/',views.AddProduct, name="AddProduct"),
    path('updateproduct/<str:pk>/',views.UpdateProduct, name="UpdateProduct"),
    path('deleteproduct/<str:pk>/',views.DeleteProduct, name="DeleteProduct"),
    path('deleteorder/<str:pk>/',views.DeleteOrder, name="DeleteOrder"),
    path('updateorder/<str:pk>/',views.UpdateOrder, name="UpdateOrder"),






     ]
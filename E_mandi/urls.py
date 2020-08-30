"""E_mandi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from E_mandi import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ShowIndex,name="main"),
    path('emandiprocess/',views.emandiprocess,name="emandiprocess"),
    path('admin_update/',views.admin_update,name="admin_update"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_login_check/', views.admin_login_check, name="admin_login_check"),
    path('adminhome/', views.adminhome, name="adminhome"),


    path('view_all_marchnat/',views.view_all_marchnat,name="view_all_marchnat"),
    path('view_all_farmer/',views.view_all_farmer,name="view_all_farmer"),
    path('delete_marchant/',views.delete_marchant,name="delete_marchant"),
    path('delete_farmer/',views.delete_farmer,name="delete_farmer"),
    path('admin_view_product/',views.admin_view_product,name="admin_view_product"),
    path('price_list/',views.price_list,name="price_list"),


    path('farmer_registration/',views.farmer_registration,name="farmer_registration"),
    path('save_farmer/',views.save_farmer,name="save_farmer"),
    path('farmer_login/',views.farmer_login,name="farmer_login"),
    path('farmer_login_check/',views.farmer_login_check,name="farmer_login_check"),
    path('add_product/',views.add_product,name="add_product"),
    path('save_product/',views.save_product,name="save_product"),
    path('viewall_product/',views.viewall_product,name="view_all_product"),
    path('merchant_register/',views.merchant_register,name="merchant_register"),
    path('save_marchant/',views.save_marchant,name="save_marchant"),
    path('marchantlogin/',views.marchantlogin,name="marchantlogin"),
    path('marchant_login_check/',views.marchant_login_check,name="marchant_login_check"),
    path('new_license/',views.new_license,name="new_license"),
    path('save_license/',views.save_license,name="save_license"),
    path('viewall_product1/',views.viewall_product1,name="view_all_product1"),
    path('order_product/',views.order_product,name="order_product"),
    path('view_order',views.view_order,name="view_order"),
     path('view_application/',views.view_application,name="view_application"),
    path ('admin_new_lic/',views.admin_new_lic,name="admin_new_lic"),
    path('view_lic/',views.view_lic,name="view_lic"),

    path('save_accept_app/',views.save_accept_app,name="save_accept_app"),
    path('viewPendingLic/', views.viewPendingLic, name='viewPendingLic'),
    path('viewAcceptedLic/',views.viewAcceptedLic,name="viewAcceptedLic"),
    path('viewRejectedLic/',views.viewRejectedLic,name="viewRejectedLic"),
    path('reject_app/',views.reject_app,name="reject_app"),


    path('contact_us/',views.contact_us,name="contact_us"),
    path('feedback/',views.comlaint_feedback,name="feedback"),
    path('send_email/',views.send_email,name="send_email")


]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

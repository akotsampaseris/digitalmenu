from django.urls import path

from . import views

app_name = 'shops'

urlpatterns = [
    path('catalogue', views.catalogue, name='catalogue'),
    path('<str:slug>', views.view_shop, name='view_shop'),
    path('create/shop', views.create_shop, name='create_shop'),
    path('<str:slug>/edit-shop', views.edit_shop, name='edit_shop'),
    path('<str:slug>/delete-shop', views.delete_shop, name='delete_shop'),

]

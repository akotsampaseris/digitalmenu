from django.urls import path

from . import views

app_name = 'menus'

urlpatterns = [
    path('<str:slug>/menus', views.view_shop_menus, name='view_shop_menus'),
    path('<str:slug>/menus/<str:name>', views.view_menu, name='view_menu'),
    path('<str:slug>/create-menu', views.create_menu, name='create_menu'),
    path('<str:slug>/create-menu/category', views.create_menu_category, name='create_menu_category'),
    path('<str:slug>/create-menu/item', views.create_menu_item, name='create_menu_item'),
]

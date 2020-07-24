from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),

    # Shop Views
    path('shops', views.view_shops, name='view_shops'),
    path('shops/create', views.create_shop, name='create_shop'),
    path('shops/<slug:slug>', views.update_shop, name='update_shop'),
    path('shops/<slug:slug>/activate', views.activate_shop, name='activate_shop'),
    path('shops/<slug:slug>/deactivate', views.deactivate_shop, name='deactivate_shop'),
    path('shops/<slug:slug>/delete', views.delete_shop, name='delete_shop'),

    # Menu Views
    path('menus', views.view_menus, name='view_menus'),
    path('<slug:slug>/menus/create', views.create_menu, name='create_menu'),
    path('menus/<int:id>', views.update_menu, name='update_menu'),
    path('menus/<int:id>/delete', views.delete_menu, name='delete_menu'),
]

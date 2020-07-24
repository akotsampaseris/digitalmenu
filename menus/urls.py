from django.urls import path

from . import views

app_name = 'menus'
urlpatterns = [
    path('menus', views.view_menu_list, name='view_list'),
    path('menu/<int:id>', views.view_menu, name='view'),
    path('menu/create', views.create_menu, name='create'),
    path('menu/<int:menu_id>/create-category',
            views.create_menu_category,
            name='create_category'),
    path('menu/<int:menu_id>/category/<int:cat_id>/create-item',
            views.create_menu_item,
            name='create_item'),
]

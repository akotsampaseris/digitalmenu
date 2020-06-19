from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics

from .models import Menu, MenuCategory, MenuItem
from .forms import MenuForm, MenuCategoryForm, MenuItemForm
from .serializers import MenuSerializer

from shops.models import Shop

# Create your views here.
def view_shop_menus(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    menus = Menu.objects.filter(shop_id=slug)

    context = {
        "shop": shop,
        "menus": menus
    }

    return render(request, 'menus/view_shop_menus.html', context)


def view_menu(request, slug, name):
    shop = get_object_or_404(Shop, slug=slug)
    menu = get_object_or_404(Menu, name=name, shop_id=slug)
    categories = MenuCategory.objects.filter(menu=menu)
    items = MenuItem.objects.filter(menu=menu)

    context = {
        "shop": shop,
        "menu": menu,
        "menu_categories": categories,
        "menu_items": items
    }

    return render(request, 'menus/view_menu.html', context)


def create_menu(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('shops:catalogue')

    else:
        form = MenuForm()

    context = {
        "form": form,
        "shop": shop
    }

    return render(request, 'menus/create_menu.html', context)


def create_menu_category(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    if request.method == "POST":
        form = MenuCategoryForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('shops:catalogue')

    else:
        form = MenuCategoryForm()

    context = {
        "form": form,
        "shop": shop
    }

    return render(request, 'menus/create_menu_category.html', context)


def create_menu_item(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('shops:catalogue')

    else:
        form = MenuItemForm()

    context = {
        "form": form,
        "shop": shop
    }

    return render(request, 'menus/create_menu_item.html', context)

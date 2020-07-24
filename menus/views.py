from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics

from .models import Menu, MenuCategory, MenuItem
from .forms import MenuForm, MenuCategoryForm, MenuItemForm
from .serializers import MenuSerializer

from shops.models import Shop

# Create your views here.
def view_menu_list(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    menus = Menu.objects.filter(shop_id=slug)

    context = {
        "shop": shop,
        "menus": menus
    }

    return render(request, 'menus/view_list.html', context)


def view_menu(request, slug, id):
    shop = get_object_or_404(Shop, slug=slug)
    menu = get_object_or_404(Menu, pk=id)
    categories = MenuCategory.objects.filter(menu=menu)
    items = MenuItem.objects.filter(menu=menu)

    context = {
        "shop": shop,
        "menu": menu,
        "menu_categories": categories,
        "menu_items": items
    }

    return render(request, 'menus/view.html', context)


def create_menu(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    if shop.owner != request.user:
        messages.warning(request, 'You do not have access to this page!')
        return redirect('menus:view_shop_menus', shop.slug)

    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            currency = form.cleaned_data['currency']
            language = form.cleaned_data['language']
            menu = Menu.objects.create(
                shop=shop,
                name=name,
                currency=currency,
                language=language
            )
            return redirect('menus:view_list', shop.slug  )

    else:
        form = MenuForm()

    context = {
        "form": form,
        "shop": shop
    }

    return render(request, 'menus/create.html', context)


def create_menu_category(request, slug, menu_id):
    shop = get_object_or_404(Shop, slug=slug)
    menu = get_object_or_404(Menu, pk=menu_id)

    if shop.owner != request.user:
        messages.warning(request, 'You do not have access to this page!')
        return redirect('shop:view', shop.slug)

    if request.method == "POST":
        form = MenuCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            menu_cat = MenuCategory.objects.create(
                menu=menu,
                name=name,
                description=description
            )
            return redirect('shops:view', shop.slug)
        else:
            messages.error(request, 'There was an error!')

    else:
        form = MenuCategoryForm()

    context = {
        "form": form,
        "shop": shop
    }

    return render(request, 'menus/create_category.html', context)


def create_menu_item(request, slug, menu_id, cat_id):
    shop = get_object_or_404(Shop, slug=slug)
    menu = get_object_or_404(Menu, pk=menu_id)

    if shop.owner != request.user:
        messages.warning(request, 'You do not have access to this page!')
        return redirect('menus:view_shop_menus', shop.slug)

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

    return render(request, 'menus/create_item.html', context)

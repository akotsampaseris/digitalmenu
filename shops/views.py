from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Shop
from .forms import ShopCreateForm, ShopEditForm
from menus.models import Menu, MenuCategory, MenuItem

# Create your views here.
def catalogue(request):
    shops = Shop.objects.all()

    context = {
        "shops": shops
    }
    return render(request, 'shops/catalogue.html', context)


def view_shop(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    menus = Menu.objects.filter(shop_id=slug)
    categories = MenuCategory.objects.all()
    items = MenuItem.objects.all()

    context = {
        "shop": shop,
        "menus": menus,
        "categories": categories,
        "items": items
    }

    return render(request, 'shops/view_shop.html', context)


def create_shop(request):
    if request.method == "POST":
        form = ShopCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shops:catalogue')
    else:
        form = ShopCreateForm()

    context = {
        "form": form
    }

    return render(request, 'shops/create_shop.html', context)


def edit_shop(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    if request.method == "POST":
        form = ShopEditForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shops:catalogue')
    else:
        form = ShopEditForm(instance=shop)

    context = {
        "form": form,
        "shop": shop
    }

    return render(request, 'shops/edit_shop.html', context)


def delete_shop(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    shop.delete()

    return redirect('shops:catalogue')

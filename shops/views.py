from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from .models import Shop, ShopWebInfo, ShopAddressInfo
from menus.models import Menu

# Create your views here.
def catalogue(request):
    shops = Shop.objects.order_by('slug')

    context = {
        "shops": shops
    }

    return render(request, 'shops/catalogue.html', context)


def view_shop(request, slug):
    shop = get_object_or_404(Shop, slug=slug)
    web_info = get_object_or_404(ShopWebInfo, shop=shop)
    add_info = get_object_or_404(ShopAddressInfo, shop=shop)
    menus = Menu.objects.filter(shop=shop)

    context = {
        "shop": shop,
        "web_info": web_info,
        "add_info": add_info,
        "menus": menus,
    }

    return render(request, 'shops/view.html', context)

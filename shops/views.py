from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Shop
from .forms import ShopForm

# Create your views here.
def catalogue(request):
    shops = Shop.objects.all()

    context = {
        "shops": shops
    }
    return render(request, 'shops/catalogue.html', context)


def view_shop(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    context = {
        "shop": shop
    }

    return render(request, 'shops/view_shop.html', context)


def create_shop(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shops:catalogue')
    else:
        form = ShopForm()

    context = {
        "form": form
    }

    return render(request, 'shops/create_shop.html', context)


def edit_shop(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    if request.method == "POST":
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shops:catalogue')
    else:
        form = ShopForm(instance=shop)

    context = {
        "form": form,
        "shop": shop
    }

    return render(request, 'shops/edit_shop.html', context)


def delete_shop(request, slug):
    shop = get_object_or_404(Shop, slug=slug)

    shop.delete()

    return redirect('shops:catalogue')

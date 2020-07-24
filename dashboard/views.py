from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages

from shops.models import Shop, ShopWebInfo, ShopAddressInfo
from menus.models import Menu, MenuCategory, MenuItem

from shops.forms import ShopForm, ShopWebInfoForm, ShopAddressInfoForm
from menus.forms import MenuForm, MenuCategoryForm, MenuItemForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')


@login_required
def settings(request):
    return render(request, 'dashboard/settings.html')


# Shop Views
@login_required
def view_shops(request):
    owner = request.user
    shops = Shop.objects.filter(owner=owner)

    context = {
        "shops": shops
    }

    return render(request, 'dashboard/shops/view_list.html', context)


@login_required
def create_shop(request):
    owner = request.user

    if request.method == "POST":
        form = ShopForm(request.POST, initial={'owner': owner})
        if form.is_valid():
            form.save()
            messages.success(request, 'You have created a new shop!')

            return redirect('dashboard:view_shops')
        else:
            messages.error(request, 'There was an error!')
    else:
        form = ShopForm(initial={'owner': owner})

    context = {
        "form": form
    }

    return render(request, 'dashboard/shops/create.html', context)


@login_required
def update_shop(request, slug):
    owner = request.user
    shop = get_object_or_404(Shop, slug=slug)
    web_info = ShopWebInfo.objects.get(shop=shop)
    address_info = ShopAddressInfo.objects.get(shop=shop)

    if owner != shop.owner:
        return redirect('dashboard:view_shops')

    if request.method == "POST":
        main_form = ShopForm(request.POST, instance=shop)
        web_form = ShopWebInfoForm(request.POST, instance=web_info)
        address_form = ShopAddressInfoForm(request.POST, instance=address_info)

        if request.POST['form_id'] == 'main-info':
            if main_form.is_valid():
                main_form.save()
                messages.success(request, 'Your changes have been saved!')
            else:
                messages.error(request, 'There was an error with your main info!')
        elif request.POST['form_id'] == 'web-info':
            if web_form.is_valid():
                web_form.save()
                messages.success(request, 'Your changes have been saved!')
            else:
                messages.error(request, 'There was an error with your web info!')
        elif request.POST['form_id'] == 'address-info':
            if address_form.is_valid():
                address_form.save()
                messages.success(request, 'Your changes have been saved!')
            else:
                messages.error(request, 'There was an error with your address info!')
        return redirect('dashboard:update_shop', shop.slug)
    else:
        main_form = ShopForm(instance=shop)
        web_form = ShopWebInfoForm(instance=web_info)
        address_form = ShopAddressInfoForm(instance=address_info)


    context = {
        "shop": shop,
        "main_form": main_form,
        "web_form": web_form,
        "address_form": address_form
    }

    return render(request, 'dashboard/shops/update.html', context)


@login_required
def activate_shop(request, slug):
    owner = request.user
    shop = Shop.objects.get(slug=slug)

    if owner != shop.owner:
        return redirect('dashboard:view_shops')

    shop.is_active = True
    shop.save()

    context = {
        "shop": shop
    }

    return redirect('dashboard:view_shops')


@login_required
def deactivate_shop(request, slug):
    owner = request.user
    shop = Shop.objects.get(slug=slug)

    if owner != shop.owner:
        return redirect('dashboard:view_shops')

    shop.is_active = False
    shop.save()

    context = {
        "shop": shop
    }

    return redirect('dashboard:view_shops')


@login_required
def delete_shop(request, slug):
    owner = request.user
    shop = Shop.objects.get(slug=slug)

    if owner != shop.owner:
        return redirect('dashboard:view_shops')

    shop.delete()

    return redirect('dashboard:view_shops')


# Menu Views
@login_required
def view_menus(request):
    owner = request.user
    shops = Shop.objects.filter(owner=owner)
    menus = Menu.objects.filter(owner=owner)

    if request.method == "POST":
        try:
            slug = request.POST['shops']
            return redirect('dashboard:create_menu', slug)
        except:
            messages.error(request, 'You must select a shop!')

    context = {
        "shops": shops,
        "menus": menus
    }

    return render(request, 'dashboard/menus/view_list.html', context)


@login_required
def create_menu(request, slug):
    owner = request.user
    shop = Shop.objects.get(slug=slug)

    if request.method == "POST":
        form = MenuForm(request.POST, initial={'owner': owner, 'shop': shop})
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have created a new menu!')

            return redirect('dashboard:view_menus')
        else:
            messages.error(request, 'There was an error!')
    else:
        form = MenuForm(initial={'owner': owner, 'shop': shop})

    context = {
        "form": form
    }

    return render(request, 'dashboard/menus/create.html', context)


@login_required
def update_menu(request, id):
    owner = request.user
    menu = Menu.objects.get(pk=id)

    if owner != menu.owner:
        return redirect('dashboard:view_shops')

    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your changes have been saved!')
            return redirect('dashboard:update_menu', menu.id)
        else:
            messages.error(request, 'There was an error!')

    else:
        form = MenuForm(instance=menu)


    context = {
        "menu": menu,
        "form": form
    }

    return render(request, 'dashboard/menus/update.html', context)


@login_required
def delete_menu(request, id):
    owner = request.user
    menu  = Menu.objects.get(pk=id)

    if owner != menu.owner:
        return redirect('dashboard:view_menus')

    menu.delete()

    return redirect('dashboard:view_menus')

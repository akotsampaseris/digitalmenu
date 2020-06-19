from django import forms

from .models import Menu, MenuCategory, MenuItem

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"


class MenuCategoryForm(forms.ModelForm):
    class Meta:
        model = MenuCategory
        fields = "__all__"


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

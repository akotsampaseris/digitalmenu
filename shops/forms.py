from django import forms

from .models import Shop

class ShopForm(forms.ModelForm):
    slug = forms.CharField(disabled=True)
    address_2 = forms.CharField(required=False)
    class Meta:
        model = Shop
        fields = "__all__"

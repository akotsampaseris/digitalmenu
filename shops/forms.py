from django import forms

from .models import Shop, ShopWebInfo, ShopAddressInfo

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = '__all__'
        widgets = {
            'owner': forms.HiddenInput(),
            'is_active': forms.HiddenInput()
            }


class ShopWebInfoForm(forms.ModelForm):
    class Meta:
        model = ShopWebInfo
        fields = '__all__'
        widgets = {'shop': forms.HiddenInput()}


class ShopAddressInfoForm(forms.ModelForm):
    class Meta:
        model = ShopAddressInfo
        fields = '__all__'
        widgets = {'shop': forms.HiddenInput()}

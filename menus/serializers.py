from rest_framework import serializers

from .models import Menu, MenuItem, MenuCategory

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"

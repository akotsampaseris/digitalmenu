from django.urls import path

from . import views

app_name="shops"
urlpatterns = [
    path('catalogue', views.catalogue, name="catalogue"),
]

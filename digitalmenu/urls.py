from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie

urlpatterns = [
    # Django Apps
    path('admin/', admin.site.urls),
    # GraphQL API
    path('api/', csrf_exempt(jwt_cookie(GraphQLView.as_view()))),
    # Custom Apps
    path('', include('frontend.urls')),
]
"""
path('', include('pages.urls')),
path('shops/', include('shops.urls')),
path('menus/', include('menus.urls')),"""

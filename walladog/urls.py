"""walladog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from users.api import UserViewSet
from categories.api import CategoryViewSet
from races.api import RacesViewSet

#APIRouter
router = DefaultRouter()
router.register(r'api/1.0/users', UserViewSet, base_name='user')
router.register(r'api/1.0/categories', CategoryViewSet, base_name='category')
router.register(r'api/1.0/races', RacesViewSet, base_name='race')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/1.0/login/', include('rest_framework.urls',namespace='rest_framework')),

    # API URLs
    url(r'', include(router.urls)),
]

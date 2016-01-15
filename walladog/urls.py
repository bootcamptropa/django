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
from saveserches.api import SaveSerchesViewSet
from users.api import UserViewSet, LoginViewSet
from categories.api import CategoryViewSet
from races.api import RacesViewSet
from states.api import StatesViewSet
from products.api import ProductsViewSet, FileUploadView

#APIRouter
router = DefaultRouter()
router.register(r'api/1.0/users', UserViewSet, base_name='user')
router.register(r'api/1.0/categories', CategoryViewSet, base_name='category')
router.register(r'api/1.0/races', RacesViewSet, base_name='race')
router.register(r'api/1.0/states', StatesViewSet, base_name='states')
router.register(r'api/1.0/products', ProductsViewSet, base_name='product')
router.register(r'api/1.0/serches', SaveSerchesViewSet, base_name='search')
router.register(r'api/1.0/logins', LoginViewSet, base_name='login')

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^send-file/', FileUploadView.as_view(), name='upload_to_s3'),
]

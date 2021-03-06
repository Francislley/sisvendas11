"""vendas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

#imports of lib Rest_frameorw
from rest_framework import routers
from core.views import CustomerViewSet, SellerViewSet, CategoryViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]

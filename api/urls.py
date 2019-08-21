from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet
from django.urls import path
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    path('wallet/', create_wallet, name='create_wallet'),
]
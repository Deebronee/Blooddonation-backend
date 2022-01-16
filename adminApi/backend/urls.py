from django.db import router
from django.urls import path, include
from rest_framework import routers


#URLConf
router = routers.DefaultRouter()


urlpatterns =[
    path('', include(router.urls)),
]
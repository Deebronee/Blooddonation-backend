from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

#URLConf
urlpatterns =[
    path('hello/',views.say_hello)
]
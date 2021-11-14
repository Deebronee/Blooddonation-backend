from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers

#URLConf
router = routers.DefaultRouter()
router.register(r'appointments',views.ApintmentsViewSet)


urlpatterns =[
    path('', include(router.urls)),
    #path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),

    #path('blood_donation_free_appointments/', views.blood_donation_free_appointmentsList.as_view()),
    #path('blood_donation_free_appointments/<int:pk>', views.blood_donation_free_appointmentsDetail.as_view()),
]

from django.db import router
from django.urls import path, include
from . import views
from rest_framework import routers


#URLConf
router = routers.DefaultRouter()
#router.register(r'appointments',views.ApintmentsViewSet) #registers the rout to appointments



urlpatterns =[
    path('', include(router.urls)),
    

    path('appointments', views.freeAppointmentsView.as_view()),
    path('appointment_status', views.appointmentStatusView.as_view()),
    path('appointment', views.appointmentCreate.as_view()),

    path('donationquestions', views.donationQuestionList.as_view()),
    path('faqquestions', views.faqQuestionsList.as_view()),
    # todo onboardingpages
    # todo request, capacities only via socket
    
    
    #path("free_appointments/", include("rest_framework.urls", namespace="rest_framework")),
    #path('reserved_appointments/', views.reserved_appointmentsList.as_view()),
    #path('assigned_appointments/', views.assigned_appointmentsList.as_view()),
    #path('appointment/', views.free_appointmentList.as_view()),
    path('request/', views.requestList.as_view()),
    path('person/', views.personList.as_view()),
    path('capacity/', views.capacityList.as_view()),
    #path('', views.index, name = 'index')
]
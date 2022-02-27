from django.db import router
from django.urls import path, include
from .views import appointmentViews, donationQuestionView, faqQuestionView, personView
from rest_framework import routers


#URLConf
router = routers.DefaultRouter()
#router.register(r'appointments',views.ApintmentsViewSet) #registers the rout to appointments



urlpatterns =[
    path('', include(router.urls)),
    

    path('appointments', appointmentViews.freeAppointmentsView.as_view()),
    path('appointment_status', appointmentViews.appointmentStatusView.as_view()),
    path('appointment', appointmentViews.appointmentCreate.as_view()),
    path('appointment_cancel', appointmentViews.appointmentCancel.as_view()),
    #path('appointment/<int:pk>', views.appointmentDetail.as_view()),
    path('donationquestions', donationQuestionView.donationQuestionList.as_view()),
    path('faqquestions', faqQuestionView.faqQuestionsList.as_view()),

    # todo onboardingpages
    # todo request, capacities only via socket
    
    
    #path("free_appointments/", include("rest_framework.urls", namespace="rest_framework")),
    #path('reserved_appointments/', views.reserved_appointmentsList.as_view()),
    #path('assigned_appointments/', views.assigned_appointmentsList.as_view()),
    #path('appointment/', views.free_appointmentList.as_view()),
    #path('request/', views.requestList.as_view()),
    path('person/', personView.personList.as_view()),
    #path('capacity/', views.capacityList.as_view()),
    #path('', views.index, name = 'index')
]
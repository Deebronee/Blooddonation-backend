from rest_api.models.statistic import Statistic
from django.db.models import F


def totalBookedAppointments():

    if Statistic.objects.all().count() == 0:
        stat = Statistic(
            numberOfFirstTimeDonations = 0,
            totalBookedAppointments = 0,
            aged18to27 = 0,
            aged28to37 = 0,
            aged38to47 = 0,
            aged48to57 = 0,
            aged58to68 = 0,
            acceptedRequests = 0,
            rejectedRequests = 0,
            cancelledRequests = 0
        )
        stat.save()
    else:
        stat = Statistic.objects.all().first()
        stat.totalBookedAppointments += 1
        stat.save()

    

def cancelledRequests():
    
    if Statistic.objects.all().count() == 0:
        stat = Statistic(
            numberOfFirstTimeDonations = 0,
            totalBookedAppointments = 0,
            aged18to27 = 0,
            aged28to37 = 0,
            aged38to47 = 0,
            aged48to57 = 0,
            aged58to68 = 0,
            acceptedRequests = 0,
            rejectedRequests = 0,
            cancelledRequests = 0
        )
        stat.save()
    else:
        stat = Statistic.objects.all().first()
        stat.totalBookedAppointments += 1
        stat.save()


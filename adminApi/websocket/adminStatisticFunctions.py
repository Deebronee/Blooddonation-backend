from websocket.models.statistic import Statistic
from django.db.models import F

def createStatisticObj():
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


def numberOfFirstTimeDonations():

    createStatisticObj()
    
    stat = Statistic.objects.all().first()
    stat.numberOfFirstTimeDonations += 1
    stat.save()


def aged18to27():

    createStatisticObj()

    stat = Statistic.objects.all().first()
    stat.aged18to27 += 1
    stat.save()

def aged28to37():

    createStatisticObj()

    stat = Statistic.objects.all().first()
    stat.aged28to37 += 1
    stat.save()

def aged38to47():

    createStatisticObj()

    stat = Statistic.objects.all().first()
    stat.aged38to47 += 1
    stat.save()

def aged48to57():

    createStatisticObj()

    stat = Statistic.objects.all().first()
    stat.aged38to47 += 1
    stat.save()

def aged58to68():

    createStatisticObj()

    stat = Statistic.objects.all().first()
    stat.aged58to68 += 1
    stat.save()


def acceptedRequests():

    createStatisticObj()

    stat = Statistic.objects.all().first()
    stat.acceptedRequests += 1
    stat.save()


def rejectedRequests():

    createStatisticObj()

    stat = Statistic.objects.all().first()
    stat.rejectedRequests += 1
    stat.save()
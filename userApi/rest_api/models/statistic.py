from django.db import models

class Statistic(models.Model):

    numberOfFirstTimeDonations = models.IntegerField()
    totalBookedAppointments = models.IntegerField()
    aged18to27 = models.IntegerField()
    aged28to37 = models.IntegerField()
    aged38to47 = models.IntegerField()
    aged48to57 = models.IntegerField()
    aged58to68 = models.IntegerField()
    acceptedRequests = models.IntegerField()
    rejectedRequests = models.IntegerField()
    cancelledRequests = models.IntegerField()

    class Meta:
        db_table = "Statistic"

  
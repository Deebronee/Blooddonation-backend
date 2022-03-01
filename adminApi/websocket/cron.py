from models.appointment import Appointment
import datetime


def cron_job():
    time = datetime.datetime.now() - datetime.timedelta(days = 14) 
    objects_to_delete = Appointment.objects.filter(Appointment.start<=time)
    objects_to_delete.delete()
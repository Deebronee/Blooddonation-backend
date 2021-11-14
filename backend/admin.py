from django.contrib import admin

from .models import blood_donation_appointments
from .models import blood_donation_free_appointments
from .models import Individual_appointment
 # how das the admin interface looks loke
# Register your models here.
admin.site.register(blood_donation_appointments)
admin.site.register(blood_donation_free_appointments)
admin.site.register(Individual_appointment)
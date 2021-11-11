from django.contrib import admin

from .models import blood_donation_appointments
from .models import blood_donation_free_appointments
 # how das the admin interface looks loke
# Register your models here.
admin.site.register(blood_donation_appointments)
admin.site.register(blood_donation_free_appointments)
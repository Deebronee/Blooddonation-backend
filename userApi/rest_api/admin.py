from django.contrib import admin

from rest_api.models.appointment import Appointment
from rest_api.models.donationQuestion import DonationQuestion
from rest_api.models.person import Person
from rest_api.models.request import Request
from rest_api.models.capacity import Capacity

# how das the admin interface looks loke
# Register your models here. To see them in the admin interface

admin.site.register(Appointment)
admin.site.register(DonationQuestion)
admin.site.register(Person)
admin.site.register(Request)
admin.site.register(Capacity)
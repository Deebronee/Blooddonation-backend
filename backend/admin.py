from django.contrib import admin

from backend.models.appointment import Appointment
from backend.models.donationQuestion import DonationQuestion
from backend.models.person import Person
from backend.models.request import Request
from backend.models.capacity import Capacity

# how das the admin interface looks loke
# Register your models here. To see them in the admin interface

admin.site.register(Appointment)
admin.site.register(DonationQuestion)
admin.site.register(Person)
admin.site.register(Request)
admin.site.register(Capacity)
from django.contrib import admin

from backend.models.appointment import appointment
from backend.models.donationQuestion import donationQuestion
from backend.models.person import person
from backend.models.request import request
from backend.models.capacity import capacity

# how das the admin interface looks loke
# Register your models here. To see them in the admin interface

admin.site.register(appointment)
admin.site.register(donationQuestion)
admin.site.register(person)
admin.site.register(request)
admin.site.register(capacity)
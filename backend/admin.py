from django.contrib import admin

from .models import blood_donation_appointments, kill_questions
 # how das the admin interface looks loke
# Register your models here. To see them in the admin interface

admin.site.register(blood_donation_appointments)
admin.site.register(kill_questions)
from django.contrib import admin

from backend.models.appointments import appointments
from backend.models.kill_questions import kill_questions
 # how das the admin interface looks loke
# Register your models here. To see them in the admin interface

admin.site.register(appointments)
admin.site.register(kill_questions)
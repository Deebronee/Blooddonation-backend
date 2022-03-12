from django.contrib import admin

from websocket.models.appointment import Appointment
from websocket.models.capacity import Capacity
from websocket.models.donationQuestion import DonationQuestion
from websocket.models.donationQuestionTranslation import DonationQuestionTranslation
from websocket.models.faqQuestion import FaqQuestion
from websocket.models.faqQuestionTranslation import FaqQuestionTranslation
from websocket.models.onboardingPage import OnboardingPage
from websocket.models.person import Person
from websocket.models.request import Request
from websocket.models.statistic import Statistic



# how the admin interface looks like
# Register your models here. To see them in the admin interface

admin.site.register(Appointment)
admin.site.register(Capacity)
admin.site.register(DonationQuestion)
admin.site.register(DonationQuestionTranslation)
admin.site.register(FaqQuestion)
admin.site.register(FaqQuestionTranslation)
admin.site.register(OnboardingPage)
admin.site.register(Person)
admin.site.register(Request)
admin.site.register(Statistic)

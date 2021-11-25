import json
from channels.generic.websocket import WebsocketConsumer
from django.db.models.query import RawQuerySet
from backend.models.appointments import appointments
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
import time

class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        all_appointments = []
        models = appointments.objects.all
        for model in models:
            new_data = model_to_dict(model)
        self.send(json.dumps({'appointments' : all_appointments}))


    #@receiver(post_save, sender=appointments)
    #def updateSocket(sender, **kwargs):
        #count = 'Franz'
        #send(json.dumps({'message' : count}))
    
    def disconnect(self, close_code):
        pass

   # def receive(self, text_data):

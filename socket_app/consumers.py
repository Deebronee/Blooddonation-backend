import json
from channels.generic.websocket import WebsocketConsumer
from django.db.models.query import RawQuerySet
from backend.models.appointments import appointments
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
import time

def createModelDict():
    appDict = []
    count = 0
    all_appointments = appointments.objets.all
    for app in all_appointments:
        appDict[count] = {
            'id' : app.id,
            'date' : app.date,
            'last_name' : app.last_name,
            'first_name': app.first_name,
            'reserved' : app.reserved,
            'assigned': app.assigned}
    return appDict



class WSConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        test = 0
        self.send(json.dumps({'message' : test}))
        #while True:
        #    self.send(json.dumps({'message' : test}))
        #    test += 1
        #    time.sleep(1)


    #@receiver(post_save, sender=appointments)
    #def updateSocket(sender, **kwargs):
        #count = 'Franz'
        #send(json.dumps({'message' : count}))
    
    def disconnect(self, close_code):
        pass

   # def receive(self, text_data):

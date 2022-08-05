

# this is for company -- ki user ni subscribe kel ki company la mahiti padel 
#   ki this user ne subscribe kela aahe 

# for signals
from django.dispatch import Signal, receiver

new_subscriber = Signal(providing_args=['job', 'subscriber'])
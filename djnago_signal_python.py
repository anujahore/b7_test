

from django.dispatch import Signal, receiver

# create custome signal
ping_signal = Signal(providing_args=["context"])


class SignalDemo:
    def ping(self):
        '''
        this functions is to send the signal
        '''
        print('PING')
        ping_signal.send(self.__class__, PING=True, val=23)


@receiver(ping_signal)
def pong(**kwargs):
    '''
    this function is to receive the signal
    '''
    print('in pong')
    print(kwargs)  #--> output in dict {'signal': <django.dispatch.dispatcher.Signal object at 0x000001F809C0BE20>, 'sender': <class '__main__.SignalDemo'>, 'PING': True, 'val': 23}
    if kwargs['PING']:
        print('PONG')

demo = SignalDemo()
demo.ping()
# PING
# in pong
# {'signal': <django.dispatch.dispatcher.Signal object at 0x0000014A9071BE20>, 'sender': <class '__main__.SignalDemo'>, 'PING': True, 'val': 23}
# PONG


# create custome signal
ping_signal = Signal(providing_args=["context"])


class SignalDemo:
    def ping(self):
        '''
        this functions is to send the signal
        '''
        print('PING')
        ping_signal.send(self.__class__, PING=False, val=23)


@receiver(ping_signal)
def pong(**kwargs):
    '''
    this function is to receive the signal
    '''
    print('in pong')
    print(kwargs)  #--> output in dict {'signal': <django.dispatch.dispatcher.Signal object at 0x000001F809C0BE20>, 'sender': <class '__main__.SignalDemo'>, 'PING': True, 'val': 23}
    if kwargs['PING']:
        print('PONG')

demo = SignalDemo()
demo.ping()
# PING
# in pong
# {'signal': <django.dispatch.dispatcher.Signal object at 0x00000206B638BD00>, 'sender': <class '__main__.SignalDemo'>, 'PING': False, 'val': 23}

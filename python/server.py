###############################################################################
##
##
##
###############################################################################

from autobahn.twisted.websocket import WebSocketServerProtocol#, \
                                       #WebSocketServerFactory
from autobahn.twisted.websocket import WebSocketServerFactory
import sys
import RPi.GPIO as gpio
import time
import os
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#set mode to BCM for pin layout and setup all GPIOs as output
def setupAllPins() :
        gpio.setmode(gpio.BCM)
        gpio.setup(2, gpio.OUT)
        gpio.setup(3, gpio.OUT)
        gpio.setup(4, gpio.OUT)
        gpio.setup(17, gpio.OUT)
        gpio.setup(27, gpio.OUT)
        gpio.setup(22, gpio.OUT)
        gpio.setup(10, gpio.OUT)
        gpio.setup(9, gpio.OUT)
        gpio.setup(11, gpio.OUT)
        gpio.setup(5, gpio.OUT)
        gpio.setup(6, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(19, gpio.OUT)
        gpio.setup(26, gpio.OUT)
        gpio.setup(14, gpio.OUT)
        gpio.setup(15, gpio.OUT)
        gpio.setup(18, gpio.OUT)
        gpio.setup(23, gpio.OUT)
        gpio.setup(24, gpio.OUT)
        gpio.setup(25, gpio.OUT)
        gpio.setup(8, gpio.OUT)
        gpio.setup(7, gpio.OUT)
        gpio.setup(12, gpio.OUT)
        gpio.setup(16, gpio.OUT)
        gpio.setup(20, gpio.OUT)
        gpio.setup(21, gpio.OUT)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#to turn a relay True set the signal pin to = False
#to turn a relay off set the signal pin to = True
#yes it is counter intuitive...deal with it.

def turnOnGPIO(pin):
    gpio.output(int(pin), False)
    print("GPIO %s on" % pin)
    
def turnOffGPIO(pin):
    gpio.output(int(pin), True)
    print("GPIO %s off" % pin)
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------



class MyServerProtocol(WebSocketServerProtocol):
   
   def onConnect(self, request):
      print("Client connecting: {0}".format(request.peer))
      
   def onOpen(self):
      print("WebSocket connection open.")

   def onMessage(self, payload, isBinary):
      if isBinary:
         print("Binary message received: {0} bytes".format(len(payload)))
      else:
         print("Text message received: {0}".format(payload.decode('utf8')))
         
         #assign the message payload to a variable 
         client_msg = format(payload.decode('utf8'))

         #partition client_msg into pin and command vars
         t = client_msg.partition(" ")
         pin = t[0]
         command = t[2]
         
	 #decide what to do
         if command == "on":
             print("Turning On GPIO %s " % pin)
             turnOnGPIO(pin)
         elif command == "off":
             print("Turning Off GPIO %s " % pin)
             turnOffGPIO(pin)
            
      ## echo back message verbatim
      self.sendMessage(payload, isBinary)

   def onClose(self, wasClean, code, reason):
      print("WebSocket connection closed: {0}".format(reason))


    
if __name__ == '__main__':
    try:
       import sys
       from twisted.python import log
       from twisted.internet import reactor
       
       log.startLogging(sys.stdout)
    
       factory = WebSocketServerFactory("ws://localhost:8765", debug = True)
    
       factory.protocol = MyServerProtocol
       setupAllPins()    
       reactor.listenTCP(8765, factory)
       reactor.run()
    except KeyboardInterrput:
        gpio.cleanup()
        print("Clean goodbye")
       

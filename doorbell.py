# Ring a doorbell with a Raspberry Pi
from RPi import GPIO
import time
import urllib
import twit
from string import Template

messages = [line.strip() for line in open('messages','r').readlines()]

# GPIO pin 9 takes the bell push switch
PUSH = 9
BELL = 10

GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(PUSH,GPIO.IN)
GPIO.setup(BELL,GPIO.OUT)

rings = 0

while True:
  start = time.time()
  while GPIO.input(PUSH):
    pass
  end = time.time()
  if end-start > 0.05:
    rings = rings + 1
    try:
      urllib.urlopen('http://mini.local:8888/')
    except:
      print 'something went wrong contacting the shed'
    try:
      GPIO.output(BELL,True)
      time.sleep(0.1)
      GPIO.output(BELL,False)
    except:
      print 'something went wrong ringing the bell'
    # TODO: switch between messages
    template = Template('@mr_goodwin '+messages[rings%len(messages)])
    message = template.substitute({'time':time.strftime("%H:%M", time.localtime())});
    print 'message is '+message
    twit.tweet(message)

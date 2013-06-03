# Ring a doorbell with a Raspberry Pi
from RPi import GPIO
import time
import urllib
import twit

messages = [line.strip() for line in open('messages','r').readlines()]

# GPIO pin 9 takes the bell push switch
PUSH = 9

GPIO.setmode(GPIO.BCM) #numbering scheme that corresponds to breakout board and pin layout
GPIO.setup(PUSH,GPIO.IN)

rings = 0

while True:
  start = time.time()
  while GPIO.input(PUSH):
    pass
  end = time.time()
  if end-start > 0.2:
    rings = rings + 1
    try:
      urllib.urlopen('http://mini.local:8888/')
    except:
      pass
    # TODO: switch between messages
    twit.tweet('@mr_goodwin '+messages[rings%len(messages)])

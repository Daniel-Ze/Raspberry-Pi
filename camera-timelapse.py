import time
import RPi.GPIO as GPIO
from picamera import PiCamera

GPIO.setmode(GPIO.BOARD)
camera = PiCamera()

i = 1
take_pic = 1
GPIO.setup(11, GPIO.OUT)
GPIO.setup(11, GPIO.LOW)
while take_pic == 1:
    camera.start_preview()
    GPIO.setup(11, GPIO.HIGH)
    time.sleep(5)
    camera.capture('/home/pi/time-lapse/image%s.jpg' % i)
    i += 1
    camera.stop_preview()
    GPIO.setup(11, GPIO.LOW)
    time.sleep(20)                                      

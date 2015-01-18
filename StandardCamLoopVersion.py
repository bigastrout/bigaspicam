# First enter the command "sudo idle & " in LXTerminal to start the Python enviroment
# Open this file in the Python Shell and press F5 to rum
# This file is based on the Tutorial "PYTHON PICAMERA SETUP" By Dave Jones author of python-picamera
#www.raspberrypi.org/learning/python-picamera-setup/
# Commented and Edited for personal use By Matt Wooten 1-18-15
# Connect a momentary push buton to GPIO 27 and Ground
##################################################

# CAMERA PROGRAMIMG : Standard Camera Loop Version
# the first button press give you a preview window
# the second button press takes a pic and saves it to a new file each time
# and the program loops back to its begining
# note this file will overwrite any files that exist before the scrip is started
import time
import picamera
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, GPIO.PUD_UP)

with picamera.PiCamera() as camera:
    frame = 1
    while True:
# the next line says wait for button press to take pic
        GPIO.wait_for_edge (27, GPIO.FALLING)
# the next line starts a preview window
        camera.start_preview()
       
# a  delay to debounce the push button
        time.sleep(1)

# wait for button press to stop try RISING
        GPIO.wait_for_edge (27, GPIO.RISING)

# camera.capture takes a pic and saves it to "image1.jpg"
        camera.capture('/home/pi/PythonPicam/StandardCamLoopVersionPics/frame%03d.jpg' % frame)
        frame += 1

# camera.stop_preview stops the preview and the scrip ends
        camera.stop_preview()
# Debug
        print("Thats a good shot")
    
